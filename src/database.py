# database.py  
# Vulnerabilidad 4: "Base de datos" en texto plano  
users = {  
    "admin": {"password": "supersecret123", "role": "admin"},  
    "user1": {"password": "password123", "role": "user"}  
}  

def get_user_data(query):  
    # Vulnerabilidad 5: Inyección de diccionario (simulado)  
    return eval(f"users{query}")  # Ej: input: "['admin']"  