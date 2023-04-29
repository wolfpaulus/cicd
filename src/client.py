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
    print(f"Checking {health_url}")
    req = urllib.request.Request(health_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        return response.status == 200


def remote_json_check(number: int) -> str:
    url = f"{service_url}{number}"
    print(f"Checking {url}")
    req = urllib.request.Request(url, headers= {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json'})
    with urllib.request.urlopen(req) as response:
        if response.status != 200:
            raise Exception(f"Error: {response.status}")
        my_dict = json.loads(response.read().decode('utf-8'))
        return str(my_dict)


if __name__ == "__main__":
    if get_health():
        for i in range(7,10):
            print(f"{i} is odd: {remote_json_check(i)}")
