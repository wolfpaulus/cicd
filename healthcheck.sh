#!/bin/bash
# This script is used to check the health of the application
# By default, CMD ["python3.11", "src/ws.py"] will launch the ws.py application.
# However, this can be changed by providing a different command when running the container.
# I.e. docker run <container-id> /cicd/healthcheck.sh
# This script will launch the ws.py application, wait for 2 seconds and then check the health of the application.
# It will then kill the application and exit with 0 if the health check was OK, otherwise it will exit with 1.

(python3.11 src/ws.py) &
spid=$!
sleep 2
status=$(curl -L http://localhost:8080/health -o /dev/null -w '%{http_code}\n' -s)
kill $spid
if [ $status -eq 200 ]; then
    echo "Health check was OK $status"
    exit 0
else
    echo "Health check failed with $status"
    exit 1
fi