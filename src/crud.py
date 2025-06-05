# crud.py  
from src.database import users  

def create_user(username, password):  
    # Vulnerabilidad 6: Almacenar contraseña en texto plano  
    users[username] = {"password": password, "role": "user"}  

def delete_user(username):  
    # Vulnerabilidad 7: No verificar permisos  
    del users[username]  