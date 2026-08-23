"""
[DNA_TAG]
ORIGIN: Moto4_A9
PILLAR: valet_concierge
PATH: vibe_bridge.py
LAST_SYNC: 2026-08-02T01:12:58Z
[/DNA_TAG]
"""
import subprocess
import sys
import os
from pathlib import Path
from integrator import broadcast_migration

def run_vibe_wrapped():
    """Wraps the original Vibe CLI to bridge events."""
    # Find original vibe executable (assuming it's in the path)
    original_vibe = subprocess.run(["which", "vibe"], capture_output=True, text=True).stdout.strip()
    
    if not original_vibe:
        print("Error: Could not find original 'vibe' command.")
        sys.exit(1)
        
    # Execute original command with passed arguments
    result = subprocess.run([original_vibe] + sys.argv[1:], capture_output=True, text=True)
    
    # Broadcast event based on outcome
    if result.returncode == 0:
        broadcast_migration("Vibe_Command_Execution", Path(os.getcwd()), Path("SUCCESS"))
    else:
        broadcast_migration("Vibe_Command_Execution", Path(os.getcwd()), Path("FAILED"))
        
    # Pass through output
    print(result.stdout)
    print(result.stderr, file=sys.stderr)
    sys.exit(result.returncode)

if __name__ == "__main__":
    run_vibe_wrapped()
