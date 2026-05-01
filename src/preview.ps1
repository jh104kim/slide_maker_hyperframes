# 3000번 및 인근 포트(3001, 3002) 정리 후 Hyperframes 프리뷰 실행

$ports = 3000..3002
echo "Checking ports: $ports"

foreach ($port in $ports) {
    $process = Get-NetTCPConnection -LocalPort $port -ErrorAction SilentlyContinue
    if ($process) {
        $pids = $process.OwningProcess | Select-Object -Unique
        foreach ($pid in $pids) {
            echo "Killing process $pid using port $port..."
            Stop-Process -Id $pid -Force -ErrorAction SilentlyContinue
        }
    }
}

echo "Starting Hyperframes Preview on port 3000..."
npx hyperframes preview --port 3000
