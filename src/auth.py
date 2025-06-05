# auth.py  
import os  
import hmac
from dotenv import load_dotenv

load_dotenv() 

# Vulnerabilidad 1: Se reemplazó la contraseña hardcoded por una variable de entorno ✔
ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD") 

def login(username, password):  
    # Vulnerabilidad 2: Comparación de strings insegura (timing attack)  
    if password == ADMIN_PASSWORD:  
        return True  
    return False 

def reset_password(token):  
    # Vulnerabilidad 3: Uso de eval() con entrada de usuario  
    user_input = input("Token de seguridad: ")  
    return eval(f"token == {user_input}")  # ¡Peligro!  