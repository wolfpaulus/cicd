"""
Simple WebService Client, using urllib.request, making 10 requests to the WebService, after a health check.
Author: Wolf Paulus (https://wolfpaulus.com)

"""

import urllib.request
import json

server_url = "http://localhost:8080"  # change this to the URL of your WebService
service_url = f"{server_url}/?number="
health_url = f"{server_url}/health"


def get_health() -> bool:
    with urllib.request.urlopen(health_url) as response:
        return response.status == 200


def remote_is_odd(number: int) -> bool:
    url = f"{service_url}{number}"
    req = urllib.request.Request(url, headers={'Content-Type': 'application/json'})
    with urllib.request.urlopen(req) as response:
        my_dict = json.loads(response.read().decode('utf-8'))
        return my_dict['odd']


if __name__ == "__main__":
    if get_health():
        for i in range(10):
            print(f"{i} is odd: {remote_is_odd(i)}")
