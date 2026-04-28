# Sistema de información del equipo
import os
import platform

def info_sistema():
    print("=== Info del Sistema ===")
    print(f"OS: {platform.system()}")
    print(f"Version: {platform.version()}")
    print(f"Procesador: {platform.processor()}")

def listar_directorio():
    print("\n=== Archivos en directorio actual ===")
    for archivo in os.listdir("."):
        print(f"  - {archivo}")

def menu():
    print("\n1. Info del sistema")
    print("2. Listar directorio")
    print("3. Salir")
    return input("Elige opcion: ")

if __name__ == "__main__":
    while True:
        opcion = menu()
        if opcion == "1":
            info_sistema()
        elif opcion == "2":
            listar_directorio()
        elif opcion == "3":
            break
