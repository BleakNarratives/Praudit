"""
[DNA_TAG]
ORIGIN: Moto4_A9
PILLAR: valet_concierge
PATH: vibe_skill_shim.py
LAST_SYNC: 2026-08-02T01:12:58Z
[/DNA_TAG]
"""
import json
import subprocess
import sys
from pathlib import Path

# Path to installed vibe skills
SKILLS_DIR = Path.home() / ".vibe" / "skills"

def list_skills():
    """Lists available Vibe skills."""
    return [d.name for d in SKILLS_DIR.iterdir() if d.is_dir()]

def run_skill(skill_name, *args):
    """Executes a Vibe skill programmatically."""
    skill_path = SKILLS_DIR / skill_name
    if not skill_path.exists():
        return {"error": "Skill not found"}
    
    # Assuming skill can be invoked via a script or command pattern 
    # Placeholder for actual invocation logic based on skill structure
    command = ["vibe", "skill", "run", skill_name] + list(args)
    result = subprocess.run(command, capture_output=True, text=True)
    
    return {
        "status": "success" if result.returncode == 0 else "failed",
        "output": result.stdout,
        "error": result.stderr
    }

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"skills": list_skills()}))
    else:
        print(json.dumps(run_skill(sys.argv[1], *sys.argv[2:])))
