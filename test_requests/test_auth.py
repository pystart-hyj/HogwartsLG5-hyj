import requests
from requests.auth import HTTPBasicAuth

def test_oauth():
    r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/abc/123",auth=HTTPBasicAuth("abc","123"))
    print(r.text)
