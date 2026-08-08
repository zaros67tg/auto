from github import Github
from github import Auth
import os

# Authenticate using the token
auth = Auth.Token(os.environ["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"])
g = Github(auth=auth)

# Connect to your specific repository
# Format: "your-username/your-repo-name"
repo = g.get_repo("zaros67tg/dummy-repo")
