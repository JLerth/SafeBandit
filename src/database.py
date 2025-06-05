# database.py  
import bcrypt

# Vulnerabilidad 4: Se reemplazó el texto plano por contraseñas hasheadas con bcrypt ✔  
users = {  
    "admin": {"password": bcrypt.hashpw(b"supersecret123", bcrypt.gensalt()), "role": "admin"},
    "user1": {"password": bcrypt.hashpw(b"password123", bcrypt.gensalt()), "role": "user"} 
}  

def get_user_data(query):  
    # Vulnerabilidad 5: Inyección de diccionario (simulado)  
    return eval(f"users{query}")  # Ej: input: "['admin']"  