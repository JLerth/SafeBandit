# main.py
from src.auth import login

def main():
    print(" Sistema de Autenticación Vulnerable ")
    user = input("Usuario: ")
    pwd = input("Contraseña: ")

    if login(user, pwd):
        print("\n Acceso concedido")
        print(f"Bienvenido {user}!")
        
        # Simulación CRUD (opcional)
        if user == "admin":
            print("\n[ADMIN PANEL]")
            print("1. Crear usuario")
            print("2. Eliminar usuario")
    else:
        print("\n Credenciales inválidas")

if __name__ == "__main__":
    main()