import pytest


def test_list_public_repos(env):
    r = env.github.repos.list_your_repos()
    assert r.status_code ==200, "status_code should be 200 but actually = {}".format(r)



if __name__ == '__main__':
    pytest.main()
