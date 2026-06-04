import sys
import logging
from pathlib import Path
from detector import get_new_projects
from migrator import migrate_project
from patcher import patch_script
from integrator import broadcast_migration
from enforcer import enforce_lockdown

# Config
DESTINATION_ROOT = Path("/storage/emulated/0/RootBase")
HOME_DIR = Path.home()

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def run_audit():
    logging.info("Starting Praudit cycle.")
    
    # 1. Enforce lockdown
    enforce_lockdown(HOME_DIR)
    
    # 2. Detect
    projects = get_new_projects(HOME_DIR)
    
    for project in projects:
        logging.info(f"Processing project: {project.name}")
        
        # 3. Migrate
        new_path = migrate_project(project, DESTINATION_ROOT)
        
        # 4. Patch
        # Find all python files to patch
        for py_file in new_path.rglob("*.py"):
            patch_script(py_file, project, new_path)
            
        # 5. Integrate
        broadcast_migration(project.name, project, new_path)
        
    logging.info("Praudit cycle complete.")

if __name__ == "__main__":
    run_audit()
