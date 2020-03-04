import pytest
import os
from Environment import Env

@pytest.fixture(scope = "module",autouse =True)
def env():
    yield Env(username=os.environ["username"],password=os.environ["password"])
    # yield Env(token=os.environ["token"])

@pytest.fixture(scope = "module", autouse=True)
def just_print():
    print("______test_________")

