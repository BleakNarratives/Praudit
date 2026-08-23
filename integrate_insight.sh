#!/bin/bash
# CodeMentor-MVP Integration Script for insight_v2

# Configuration
PROJECT_ROOT="/storage/emulated/0/RootBase/CodeMentor-MVP"
NEW_ENGINE="~/tools/codementor_cli/insight_v2.py"
TARGET_DIR="$PROJECT_ROOT/backend/lib"

echo "Integrating insight_v2 into $PROJECT_ROOT..."

# 1. Back up existing
mv "$TARGET_DIR/ai_explain.py" "$TARGET_DIR/ai_explain.py.bak"

# 2. Deploy engine
cp "$NEW_ENGINE" "$TARGET_DIR/ai_explain.py"

# 3. Setup config
mkdir -p "$PROJECT_ROOT/config"
# User needs to ensure api.toml exists in this path
echo "Config deployment skipped: ensure $PROJECT_ROOT/config/api.toml is populated."

echo "Integration complete."
