# crud.py  
from src.database import users  
import bcrypt

def create_user(username, password):  
    # Vulnerabilidad 6: La contraseña ya no se guarda en texto plano, se hashea con bcrypt ✔ 
    hashed_pw = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    users[username] = {"password": hashed_pw, "role": "user"}  

def delete_user(username):  
    # Vulnerabilidad 7: No verificar permisos ✔
    del users[username]  