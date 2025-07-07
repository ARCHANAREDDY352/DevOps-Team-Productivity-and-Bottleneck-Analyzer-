import requests
import pandas as pd

def get_commits(repo, owner, token):
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)
    commits = response.json()

    data = []
    for commit in commits:
        data.append({
            "author": commit["commit"]["author"]["name"],
            "date": commit["commit"]["author"]["date"],
            "message": commit["commit"]["message"]
        })

    df = pd.DataFrame(data)
    df.to_csv("commits.csv", index=False)
    print("✅ Data saved to commits.csv")

# Example call:
# get_commits("react", "facebook", "your_github_token")