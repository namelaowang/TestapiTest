import pytest
import os
from Environment import Env
from configparser import ConfigParser


@pytest.fixture(scope = "module",autouse =True)
def env():
    config = ConfigParser()
    config.read(["data.ini"])
    # 1.使用环境变量读取的方式，需要吧evn设置为 data.ini下的环境名,并将"env":"test_env"设置到环境变量中
    api_root_url = config[os.environ['env']]['api_root_url']
    # 2.直接读取
    # api_root_url = config['test_env']['api_root_url']
    yield Env(api_root_url = api_root_url,username=os.environ["username"],password=os.environ["password"])
    # yield Env(token=os.environ["token"])


@pytest.fixture(scope = "module", autouse=True)
def just_print():
    print("______test_________")

