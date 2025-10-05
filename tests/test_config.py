import os

def test_env_variables():
    assert os.getenv("API_ID") is not None
    assert os.getenv("API_HASH") is not None
    assert os.getenv("CLIENT_NAME") is not None
