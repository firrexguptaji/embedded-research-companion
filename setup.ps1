Write-Host "=== First-Time Setup ==="

# Check Docker installed
if (-not (Get-Command docker -ErrorAction SilentlyContinue)) {
    Write-Host "Docker is not installed."
    pause
    exit
}

# Check Docker running
docker info > $null 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Docker Desktop is not running."
    pause
    exit
}

Write-Host "Building containers..."
docker compose build

Write-Host "Starting system..."
docker compose up -d

$gradioUrl = "http://localhost:7860"
Write-Host "Waiting for system..."

for ($i=0; $i -lt 40; $i++) {
    try {
        $response = Invoke-WebRequest -Uri $gradioUrl -UseBasicParsing -TimeoutSec 3
        if ($response.StatusCode -eq 200) { break }
    } catch {}
    Start-Sleep -Seconds 3
}

Start-Process $gradioUrl
Write-Host "Setup complete."
