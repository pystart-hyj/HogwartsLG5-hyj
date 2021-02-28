import requests

def test_demo():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        "Cookie": "hogwarts=school",
        'User-Agent': 'hogwarts'
    }
    r = requests.get(url=url, headers=header)
    print(r.headers)
    print(r.request.headers)
    assert r.status_code == 200

def test_demo1():
    url = "https://httpbin.testing-studio.com/cookies"
    header = {
        'User-Agent': 'hogwarts'
    }
    cookle_data = {
        "hogwarts":"school",
        "teacher":"AD"
    }
    r = requests.get(url=url, headers=header, cookies=cookle_data)
    print(r.headers)
    print(r.request.headers)
    assert r.status_code == 200