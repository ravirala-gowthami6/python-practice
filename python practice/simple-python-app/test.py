import os
import requests

# 1. Mundu Token load cheyali
GITHUB_TOKEN = os.environ.get("MY_GITHUB_TOKEN")

# 2. Validation (Token undo ledo check cheyadam)
# Deenni ikkade pettali, owner/repo names kante munde.
if not GITHUB_TOKEN:
    print("❌ Error: System lo 'MY_GITHUB_TOKEN' dorakaledu!")
    print("PowerShell lo idi kottandi: $env:MY_GITHUB_TOKEN='mee_token'")
    exit() # Token lekapothe ikkade script stop avthundi
REPO_OWNER = "ravirala-gowthami6"
REPO_NAME = "python-practice"

url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

# 2. Authentication Headers (Security)
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# 3. Mana Issue Details (Data we want to send)
issue_data = {
    "title": "Critical: Server Down Alert",
    "body": "Monitoring system detected that the production server is not responding. Please check.",
    "labels": ["bug", "critical"]
}

# 4. POST Request pampadam (Create cheyadam)
response = requests.post(url, json=issue_data, headers=headers)

# 5. Result check cheyadam
if response.status_code == 201: # 201 ante 'Created' ani artham
    print("✅ Success: Issue create ayyindi!")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text)  