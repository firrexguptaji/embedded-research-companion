Write-Host "Starting Embedded Research Companion..."

docker compose up -d

$gradioUrl = "http://localhost:7860"

for ($i=0; $i -lt 30; $i++) {
    try {
        $response = Invoke-WebRequest -Uri $gradioUrl -UseBasicParsing -TimeoutSec 3
        if ($response.StatusCode -eq 200) { break }
    } catch {}
    Start-Sleep -Seconds 2
}

Start-Process $gradioUrl
