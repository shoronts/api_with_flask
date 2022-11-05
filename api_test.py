import requests
import json


url = 'http://localhost:8001'

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2NzU3ODQ3OSwianRpIjoiNmJmMDE5NGEtMDYwNy00NDU2LThlOWMtZTU4ZDg3ZWNjZGI1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InNob3JvbiIsIm5iZiI6MTY2NzU3ODQ3OSwiZXhwIjoxNjcwMTcwNDc5fQ._Q5X5L2H_WiraxWtpKY9QrarnGst2KC59Oaof8ZU8Ow"


headers = {'Content-Type': 'application/json'}

token_headers = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {token}"
}


def register_api():
    payload = {
        'name': 'Md Sharif Foysal Shoron',
        'email': 'mdshariffoysalshoron@gmail.com',
        'username': 'shoron',
        'password': 'test100'
    }
    resp = requests.post(
        f"{url}/register/",
        headers=headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

def login_api():
    payload = {'username': 'shoron', 'password': 'test100'}
    resp = requests.post(
        f"{url}/login/",
        headers=headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

def logout_api():
    payload = {}
    resp = requests.get(
        f"{url}/logout/",
        headers=token_headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

def floor_get_api():
    payload = {}
    resp = requests.get(
        f"{url}/floor/",
        headers=token_headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

def floor_post_api():
    payload = {
        'name': 'test5',
        'price': '105'
    }
    resp = requests.post(
        f"{url}/floor/",
        headers=token_headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

def nft_get_api():
    payload = {}
    resp = requests.get(
        f"{url}/nft/",
        headers=token_headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

def nft_post_api():
    payload = {
        'name': 'Test Nft 5',
        'price': '505'
    }
    resp = requests.post(
        f"{url}/nft/",
        headers=token_headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

def loan_get_api():
    payload = {}
    resp = requests.get(
        f"{url}/loan/",
        headers=token_headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

def loan_post_api():
    payload = {
        'name': 'Test Loan 5',
        'price': '405'
    }
    resp = requests.post(
        f"{url}/loan/",
        headers=token_headers,
        data=json.dumps(payload, indent=4)
    )
    print(resp.text)

register_api()
# login_api()
# logout_api()
# floor_get_api()
# floor_post_api()
# nft_get_api()
# nft_post_api()
# loan_get_api()
# loan_post_api()
