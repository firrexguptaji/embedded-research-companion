Write-Host "Resetting system (this will delete models and data)..."

docker compose down -v

Write-Host "System reset complete."
