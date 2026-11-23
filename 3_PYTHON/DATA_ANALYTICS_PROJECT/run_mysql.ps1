$env:MYSQL_HOST = "localhost"
$env:MYSQL_PORT = "3306"
$env:MYSQL_DATABASE = "india_population"
$env:MYSQL_USER = "root"

if (-not $env:MYSQL_PASSWORD) {
    $securePassword = Read-Host "Enter MySQL password" -AsSecureString
    $env:MYSQL_PASSWORD = [System.Net.NetworkCredential]::new("", $securePassword).Password
}

python python/main.py
