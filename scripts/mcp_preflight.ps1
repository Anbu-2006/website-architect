<#
 mcp_preflight.ps1 - Safe PID-Targeted Windows MCP Pre-Flight & Port Reaper (v2.1)
 Synthesized from consensus recommendations across 4 Lead Reviewer AIs.
 
 1. Scans mcp_config.json for unpinned npx packages (@latest or missing version)
 2. Reaps zombie node/mcp processes bound to OAuth callback ports (e.g. 31858)
 3. Verifies ownership: NEVER kills non-node / non-mcp processes
#>
param(
  [string]$Config = "$env:USERPROFILE\.gemini\config\mcp_config.json",
  [int[]]$Ports = @(31858),
  [int]$StaleMinutes = 120,
  [switch]$Kill
)

$report = [ordered]@{ unpinned = @(); staleProcesses = @(); busyPorts = @(); reapedPids = @() }

# 1. Audit unpinned package versions in config
if (Test-Path $Config) {
  try {
    $cfg = Get-Content $Config -Raw | ConvertFrom-Json
    foreach ($s in $cfg.mcpServers.PSObject.Properties) {
      $cmd  = "$($s.Value.command)"
      $argv = (@($s.Value.args) -join " ")
      $usesNpx = ($cmd -match "npx") -or ($argv -match "npx")
      if ($usesNpx -and ($argv -match "@latest" -or $argv -notmatch "@\d")) {
        $report.unpinned += $s.Name
      }
    }
  } catch {
    Write-Warning "Could not parse $Config: $_"
  }
}

# 2. Audit and reap listeners on target OAuth callback ports
foreach ($p in $Ports) {
  $conns = Get-NetTCPConnection -LocalPort $p -State Listen -ErrorAction SilentlyContinue
  if ($conns) {
    foreach ($c in $conns) {
      $pidToKill = $c.OwningProcess
      if ($pidToKill -gt 0) {
        $proc = Get-Process -Id $pidToKill -ErrorAction SilentlyContinue
        $report.busyPorts += [pscustomobject]@{
          port = $p
          pid = $pidToKill
          name = if ($proc) { $proc.ProcessName } else { "unknown" }
        }
        # Safe termination: only kill if process name matches node or mcp
        if ($Kill -and $proc -and ($proc.ProcessName -like "*node*" -or $proc.Path -like "*mcp*")) {
          Write-Warning "Reaping lingering MCP listener: PID $pidToKill ($($proc.ProcessName)) on port $p"
          Stop-Process -Id $pidToKill -Force -ErrorAction SilentlyContinue
          $report.reapedPids += $pidToKill
          Start-Sleep -Milliseconds 300
        }
      }
    }
  }
}

$report | ConvertTo-Json -Depth 4
if ($report.busyPorts.Count -gt 0 -and -not $Kill) { exit 2 }
exit 0
