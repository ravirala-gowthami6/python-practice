import os
import requests

# GitHub Actions lo manam env set chesthunnam kabatti ikkada load avthundi
GITHUB_TOKEN = os.environ.get("MY_GITHUB_TOKEN")

# Validation
if not GITHUB_TOKEN:
    print("❌ Error: MY_GITHUB_TOKEN not found in environment!")
    exit(1)

# Configuration
REPO_OWNER = "ravirala-gowthami6"
REPO_NAME = "python-practice"
url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

issue_data = {
    "title": "Automated Alert from GitHub Actions",
    "body": "This issue was automatically created by a GitHub Actions workflow! 🚀",
    "labels": ["automation", "github-actions"]
}

# Execution
response = requests.post(url, json=issue_data, headers=headers)

if response.status_code == 201:
    print("✅ Success: Issue created automatically by GitHub Action!")
else:
    print(f"❌ Failed: {response.status_code}")
    print(response.text)