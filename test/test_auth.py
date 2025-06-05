# test_auth.py  
from src.auth import login 
import unittest 

# Se reemplazaron las aserciones directas por el uso de unittest
# para evitar problemas con el uso de assert en código optimizado.

class TestAuth(unittest.TestCase):

    def test_login_success(self):  
        self.assertTrue(login("admin", "supersecret123"))

    def test_login_failure(self):  
        self.assertFalse(login("admin", "wrongpass"))

if __name__ == "__main__":
    unittest.main()