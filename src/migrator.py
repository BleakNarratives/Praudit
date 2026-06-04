import shutil
import logging
from pathlib import Path

def get_versioned_path(destination_dir: Path, folder_name: str) -> Path:
    """Generates a versioned path to prevent overwriting."""
    base_dest = destination_dir / folder_name
    if not base_dest.exists():
        return base_dest
    
    version = 1
    while True:
        versioned_dest = destination_dir / f"{folder_name}_v{version}"
        if not versioned_dest.exists():
            return versioned_dest
        version += 1

def migrate_project(source_path: Path, destination_dir: Path) -> Path:
    """Migrates a project to the destination, creating a versioned copy if needed."""
    destination = get_versioned_path(destination_dir, source_path.name)
    
    logging.info(f"Migrating {source_path} to {destination}")
    shutil.move(str(source_path), str(destination))
    return destination

if __name__ == "__main__":
    # Test migration logic
    dest = Path.home() / "test_dest"
    dest.mkdir(exist_ok=True)
    
    test_proj = Path.home() / "test_proj"
    test_proj.mkdir(exist_ok=True)
    (test_proj / "README.md").touch()
    
    migrated = migrate_project(test_proj, dest)
    print(f"Migrated to: {migrated}")
