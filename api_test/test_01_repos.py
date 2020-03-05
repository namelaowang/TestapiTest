import pytest


def test_list_public_repos(env):
    r = env.github.repos.list_your_repos()
    # print(r.json())
    # print(r.json()[0]["name"])
    assert r.status_code ==200, "status_code should be 200 but actually = {}".format(r)
    assert r.content[0].get("id") ==245086965


def test_create_user_repos(env):
    data1 = {
        "name":"repostest",
        "description":"test repos demo",
        "homepage":"https://hongliang.com",
        "private":False,
        "has_issues":True,
        "has_projects":True,
        "has_wiki":True

    }
    r = env.github.repos.create_user_repo(json =data1)
    print(r)
    assert r.status_code == 201, "这不是201"



if __name__ == '__main__':
    pytest.main()

