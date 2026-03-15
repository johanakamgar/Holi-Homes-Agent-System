import requests

# آپ کا ویریفائیڈ ڈیٹا
TOKEN = "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"
REPO = "johanakamgar/Holi-Homes-Agent-System"

def activate_johanna():
    print("--- Johanna System Activation Start ---")
    url = f"https://api.github.com/repos/{REPO}"
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        repo_data = response.json()
        print(f"✅ Connection Successful!")
        print(f"✅ System Linked to: {repo_data['full_name']}")
        print(f"✅ Johanna is now monitoring this repository.")
    else:
        print(f"❌ Connection Failed. Error Code: {response.status_code}")
        print(f"Message: {response.json().get('message')}")

if __name__ == "__main__":
    activate_johanna()
