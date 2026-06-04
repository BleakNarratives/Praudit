import ast
import os
from pathlib import Path

class PathPatcher(ast.NodeTransformer):
    """AST transformer to identify and patch hardcoded file paths."""
    def __init__(self, old_root: Path, new_root: Path):
        self.old_root = str(old_root)
        self.new_root = str(new_root)

    def visit_Constant(self, node):
        """Replaces old root paths with new root paths in string constants."""
        if isinstance(node.value, str) and self.old_root in node.value:
            new_val = node.value.replace(self.old_root, self.new_root)
            return ast.copy_location(ast.Constant(value=new_val), node)
        return node

def patch_script(script_path: Path, old_root: Path, new_root: Path):
    """Parses, patches, and writes back the script."""
    with open(script_path, "r") as f:
        tree = ast.parse(f.read())
    
    transformer = PathPatcher(old_root, new_root)
    new_tree = transformer.visit(tree)
    ast.fix_missing_locations(new_tree)
    
    with open(script_path, "w") as f:
        f.write(ast.unparse(new_tree))

if __name__ == "__main__":
    # Example usage for verification
    test_file = Path("test_patch.py")
    test_file.write_text("path = '/home/user/project/data.json'\n")
    
    patch_script(test_file, Path("/home/user"), Path("/storage/emulated/0/RootBase"))
    
    print(f"Patched content: {test_file.read_text()}")
    test_file.unlink()
