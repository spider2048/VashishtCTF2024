echo "Socat running on port:$PORT"
socat TCP-LISTEN:$PORT,reuseaddr,fork EXEC:"./server/precise"
