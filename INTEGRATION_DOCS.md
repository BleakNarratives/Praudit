# Core Engine Documentation

## Core Kernel
The `agent_kernel.py` now provides the `CoreAgent` base class. This class unifies lifecycle management (OpenClaw) with the recursive improvement loop (Molt-V4), providing a consistent interface for all agents within the ecosystem.

## Migration & Integration
- **Event Bridge (`vibe_bridge.py`)**: Intercepts `vibe` commands and broadcasts execution status to the RootBase ecosystem.
- **Skill Shim (`vibe_skill_shim.py`)**: Programmatically exposes Vibe skills.

## Refactor
All agent shims (`openclaw_shim.py`, `molt_shim.py`) have been updated to inherit from `CoreAgent`, ensuring architectural consistency and removing legacy "ModMind" naming.
