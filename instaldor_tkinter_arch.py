#!/usr/bin/env python3

import os
import subprocess
import sys

def es_root():
    """Verifica si el script se está ejecutando como root."""
    return os.geteuid() == 0

def instalar_tkinter():
    
    VERDE = "\033[1;32m"
    AZUL = "\033[1;34m"
    ROJO = "\033[1;31m"
    FIN = "\033[0m"

    print(f"{AZUL}--- Instalador de Tkinter para Arch Linux ---{FIN}\n")

    if not es_root():
        print(f"{ROJO}[!] Error: Este script debe ejecutarse con sudo.{FIN}")
        sys.exit(1)

    try:
        # En Arch Linux, el paquete que contiene tkinter es simplemente 'tk'
        print(f"{AZUL}[*] Actualizando base de datos de paquetes e instalando 'tk'...{FIN}")
        
        # Ejecutar pacman
        subprocess.run(["pacman", "-Syu", "tk", "--noconfirm"], check=True)
        
        print(f"\n{VERDE}[+] Tkinter (paquete tk) se ha instalado correctamente.{FIN}")
        
        # Prueba rápida
        print(f"{AZUL}[*] Verificando versión de tcl/tk...{FIN}")
        subprocess.run(["python", "-m", "tkinter", "--version"])

    except subprocess.CalledProcessError as e:
        print(f"\n{ROJO}[!] Ocurrió un error durante la instalación: {e}{FIN}")
    except Exception as e:
        print(f"\n{ROJO}[!] Error inesperado: {e}{FIN}")

if __name__ == "__main__":
    instalar_tkinter()