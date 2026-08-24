# Praudit

**Code migration and enforcement audit system.**

Praudit scans codebases for compliance with project conventions, enforces coding standards, and automates migration of legacy code patterns. Integrates with the Molt agent lifecycle system.

---

## Modules

```
praudit.py              Main audit engine
agent_kernel.py         Agent execution kernel
molt_shim.py            Molt agent integration
openclaw_shim.py        OpenClaw integration
vibe_bridge.py          Vibe protocol bridge
config/                 Configuration files
```

## Features

- **Convention enforcement** — validates code against project standards
- **Legacy migration** — automatically refactors old patterns
- **Compliance reporting** — generates audit reports
- **Agent integration** — works with Molt and OpenClaw agents

## Usage

```bash
python praudit.py --help
```

---

*BleakNarratives // 2026*
