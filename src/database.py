# database.py  
import bcrypt

# Vulnerabilidad 4: Se reemplazó el texto plano por contraseñas hasheadas con bcrypt ✔  
users = {  
    "admin": {"password": bcrypt.hashpw(b"supersecret123", bcrypt.gensalt()), "role": "admin"},
    "user1": {"password": bcrypt.hashpw(b"password123", bcrypt.gensalt()), "role": "user"} 
}  

def get_user_data(query):  
    # Vulnerabilidad 5: Se eliminó el uso de eval para prevenir inyección de diccionario ✔
    return users.get(query)