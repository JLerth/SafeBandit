# test_auth.py  
from src.auth import login  

def test_login_success():  
    assert login("admin", "supersecret123") is True  

def test_login_failure():  
    assert login("admin", "wrongpass") is False  