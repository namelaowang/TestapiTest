from github import Github


class Env:
    def __init__(self,api_root_url, username, password):
        # self.github = Github("https://api.github.com", username=username,password =password)
        # self.github = Github("https://api.github.com", token=token)
        self.github = Github(api_root_url, username =username, password =password)