# ==============================================================================
# Website Architect & Master Builder — Automated Windows PowerShell Installer
# Author: Anbuselvan T. (@Anbu-2006)
# ==============================================================================

[CmdletBinding()]
param(
    [ValidateSet("global", "workspace", "local")]
    [string]$Target = "global"
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host " 🏛️  Website Architect & Master Builder — Agent Skill Installer   " -ForegroundColor Cyan
Write-Host "     Universal AI Web Building Engine by Anbuselvan T. (@Anbu-2006) " -ForegroundColor DarkGray
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""

$HomeDir = [Environment]::GetFolderPath("UserProfile")
$GlobalSkillsDir = Join-Path $HomeDir ".gemini\config\skills\website-architect"
$WorkspaceSkillsDir = Join-Path (Get-Location) ".agents\skills\website-architect"

if ($Target -eq "global") {
    $InstallPath = $GlobalSkillsDir
    Write-Host "👉 Target Destination: Global Antigravity Config ($InstallPath)" -ForegroundColor Yellow
} elseif ($Target -eq "workspace") {
    $InstallPath = $WorkspaceSkillsDir
    Write-Host "👉 Target Destination: Active Workspace ($InstallPath)" -ForegroundColor Yellow
} else {
    $InstallPath = Join-Path (Get-Location) "website-architect"
    Write-Host "👉 Target Destination: Local Directory ($InstallPath)" -ForegroundColor Yellow
}

# Ensure parent directory exists
$ParentDir = Split-Path -Parent $InstallPath
if (-not (Test-Path $ParentDir)) {
    New-Item -ItemType Directory -Path $ParentDir -Force | Out-Null
}

# Clone or pull repository
$RepoUrl = "https://github.com/Anbu-2006/website-architect.git"
if (Test-Path "$InstallPath\.git") {
    Write-Host "🔄 Updating existing installation at $InstallPath..." -ForegroundColor Green
    git -C $InstallPath pull --quiet origin main
} elseif (Test-Path $InstallPath) {
    Write-Host "📁 Updating existing directory at $InstallPath..." -ForegroundColor Green
} else {
    Write-Host "⬇️ Cloning Website Architect into $InstallPath..." -ForegroundColor Green
    git clone --depth 1 $RepoUrl $InstallPath
}

# Check Python environment
Write-Host "🐍 Verifying Python environment..." -ForegroundColor DarkGray
$PythonCmd = Get-Command python -ErrorAction SilentlyContinue
if ($PythonCmd) {
    Write-Host "📦 Installing runtime dependencies (pydantic, rich, playwright, jsonschema)..." -ForegroundColor DarkGray
    & python -m pip install -r "$InstallPath\requirements.txt" --quiet --disable-pip-version-check
    Write-Host "🎭 Installing Playwright Chromium browser..." -ForegroundColor DarkGray
    & python -m playwright install chromium
} else {
    Write-Warning "Python was not found in PATH. Please ensure Python 3.11+ is installed to run CLI scripts."
}

Write-Host ""
Write-Host "✅ Installation Complete! Website Architect is ready." -ForegroundColor Green
Write-Host "------------------------------------------------------------------" -ForegroundColor DarkGray
Write-Host "💡 How to Use:" -ForegroundColor White
Write-Host "  1. In Chat / Antigravity IDE:" -ForegroundColor Cyan
Write-Host "     Type: /website-architect build a modern fintech landing page" -ForegroundColor Gray
Write-Host "  2. In Terminal CLI:" -ForegroundColor Cyan
Write-Host "     python $InstallPath\scripts\classify_business.py --pitch 'Boutique hotel in Kyoto'" -ForegroundColor Gray
Write-Host "     python $InstallPath\scripts\section_option_previewer.py --section hero" -ForegroundColor Gray
Write-Host "==================================================================" -ForegroundColor Cyan
Write-Host ""
