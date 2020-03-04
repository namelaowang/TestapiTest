from github import Github


class Env:
    def __init__(self,  username,password):
        self.github = Github("https://api.github.com", username=username,password =password)
        # self.github = Github("https://api.github.com", token=token)