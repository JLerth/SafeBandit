# auth.py  
import os  

# Vulnerabilidad 1: Contraseña hardcoded  
ADMIN_PASSWORD = "supersecret123"  

def login(username, password):  
    # Vulnerabilidad 2: Comparación de strings insegura (timing attack)  
    if password == ADMIN_PASSWORD:  
        return True  
    return False 

def reset_password(token):  
    # Vulnerabilidad 3: Uso de eval() con entrada de usuario  
    user_input = input("Token de seguridad: ")  
    return eval(f"token == {user_input}")  # ¡Peligro!  