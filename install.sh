#!/usr/bin/env bash
# ==============================================================================
# Website Architect & Master Builder — Automated Linux/macOS Installer
# Author: Anbuselvan T. (@Anbu-2006)
# ==============================================================================

set -euo pipefail

CYAN='\033[0;36m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
GRAY='\033[0;90m'
NC='\033[0m' # No Color

echo -e ""
echo -e "${CYAN}==================================================================${NC}"
echo -e "${CYAN} 🏛️  Website Architect & Master Builder — Agent Skill Installer   ${NC}"
echo -e "${GRAY}     Universal AI Web Building Engine by Anbuselvan T. (@Anbu-2006)${NC}"
echo -e "${CYAN}==================================================================${NC}"
echo -e ""

TARGET="${1:-global}"
HOME_DIR="${HOME:-~}"
GLOBAL_DIR="${HOME_DIR}/.gemini/config/skills/website-architect"
WORKSPACE_DIR="$(pwd)/.agents/skills/website-architect"

if [ "$TARGET" = "workspace" ]; then
    INSTALL_PATH="$WORKSPACE_DIR"
    echo -e "${YELLOW}👉 Target Destination: Active Workspace ($INSTALL_PATH)${NC}"
elif [ "$TARGET" = "local" ]; then
    INSTALL_PATH="$(pwd)/website-architect"
    echo -e "${YELLOW}👉 Target Destination: Local Directory ($INSTALL_PATH)${NC}"
else
    INSTALL_PATH="$GLOBAL_DIR"
    echo -e "${YELLOW}👉 Target Destination: Global Antigravity / Claude Config ($INSTALL_PATH)${NC}"
fi

mkdir -p "$(dirname "$INSTALL_PATH")"

REPO_URL="https://github.com/Anbu-2006/website-architect.git"

if [ -d "$INSTALL_PATH/.git" ]; then
    echo -e "${GREEN}🔄 Updating existing installation at $INSTALL_PATH...${NC}"
    git -C "$INSTALL_PATH" pull --quiet origin main
elif [ -d "$INSTALL_PATH" ]; then
    echo -e "${GREEN}📁 Updating existing directory at $INSTALL_PATH...${NC}"
else
    echo -e "${GREEN}⬇️ Cloning Website Architect into $INSTALL_PATH...${NC}"
    git clone --depth 1 "$REPO_URL" "$INSTALL_PATH"
fi

# Python dependencies
if command -v python3 &>/dev/null; then
    echo -e "${GRAY}🐍 Installing runtime dependencies...${NC}"
    python3 -m pip install -r "$INSTALL_PATH/requirements.txt" --quiet --disable-pip-version-check
    echo -e "${GRAY}🎭 Installing Playwright Chromium browser...${NC}"
    python3 -m playwright install chromium || true
elif command -v python &>/dev/null; then
    echo -e "${GRAY}🐍 Installing runtime dependencies...${NC}"
    python -m pip install -r "$INSTALL_PATH/requirements.txt" --quiet --disable-pip-version-check
    echo -e "${GRAY}🎭 Installing Playwright Chromium browser...${NC}"
    python -m playwright install chromium || true
else
    echo -e "${YELLOW}⚠️ Python 3 not detected in PATH. Please install Python 3.11+ to execute scripts.${NC}"
fi

echo -e ""
echo -e "${GREEN}✅ Installation Complete! Website Architect is ready.${NC}"
echo -e "${GRAY}------------------------------------------------------------------${NC}"
echo -e "💡 How to Use:"
echo -e "  1. In Chat / Antigravity IDE:"
echo -e "     Type: ${CYAN}/website-architect build a modern fintech landing page${NC}"
echo -e "  2. In Terminal CLI:"
echo -e "     python3 ${INSTALL_PATH}/scripts/classify_business.py --pitch 'Boutique hotel in Kyoto'"
echo -e "     python3 ${INSTALL_PATH}/scripts/section_option_previewer.py --section hero"
echo -e "${CYAN}==================================================================${NC}"
echo -e ""
