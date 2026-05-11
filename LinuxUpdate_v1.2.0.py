#!/usr/bin/env python3

"""
Nombre del Script: LinuxUpdate
Autor: Hector Arango 
Github: https://github.com/hmam13
Descripcióon: Herramienta para automatizar la actualización de Linux.
Lenguaje: Python
Version: 1.2.0
"""

# ──────────────────────────────────────────────
#  Librerías
# ──────────────────────────────────────────────
from tkinter import *
from tkinter import messagebox
import os
import subprocess
import sys

# ──────────────────────────────────────────────
#  Configuración de Colores de Terminal
# ──────────────────────────────────────────────
VERDE = "\033[1;32m"
ROJO = "\033[1;31m"
AZUL = "\033[1;34m"
AMARILLO = "\033[1;33m"
FIN = "\033[0m"

# ──────────────────────────────────────────────
#  Configuración de Colores de Interfaz
# ──────────────────────────────────────────────
BG_COLOR = "#242424"      # Fondo principal
FG_COLOR = "#FFFFFF"      # Texto
FRAME_COLOR = "#2B2B2B"   # Fondo de los contenedores
BTN_GREEN = "#2eb82e"     # Botón actualizar
BTN_RED = "#cc0000"       # Botón cerrar
BTN_GRAY = "#3d3d3d"      # Botón ayuda
SELECT_COLOR = "#3a3a5c"  # Color cuando la distro está seleccionada

# ──────────────────────────────────────────────
#  Funciones Lógicas
# ──────────────────────────────────────────────
class Update:
    def __init__(self, ventana):
        self.venta = ventana

#  Kali Linux
    def update_kali():
        if messagebox.askquestion("Update", "¿Desea Actualizar Kali Linux?") == "yes":
            ventana.destroy()

            def ejecutar_comando(comando, titulo):
                print(f"{AZUL}{titulo}{FIN}\n")
                try:
                    subprocess.run(comando, check=True)
                except subprocess.CalledProcessError:
                    print(f"\n{ROJO}[!] Hubo un error al ejecutar {titulo} {FIN}")
                    os.system("tput cnorm")
                    sys.exit(1)
       
            def actualizacion():
                os.system("clear")
                os.system("tput civis")
                try:
                    ejecutar_comando(["sudo", "apt", "update"], "UPDATE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "apt-get", "dist-upgrade", "-y"], "UPGRADE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "apt-get", "autoremove", "-y"], "AUTOREMOVE")
                finally:
                    os.system("tput cnorm")
                    print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
       
            if os.geteuid() != 0:
                print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
                sys.exit(1)
        
            actualizacion()
# Parrot
    def update_parrot():
        if messagebox.askquestion("Update", "¿Desea Actualizar Parrot OS?") == "yes":
            ventana.destroy()

            def ejecutar_comando(comando, titulo):
                print(f"{AZUL}{titulo}{FIN}\n")
                try:
                    subprocess.run(comando, check=True)
                except subprocess.CalledProcessError:
                    print(f"\n{ROJO}[!] Hubo un error al ejecutar {titulo} {FIN}")
                    os.system("tput cnorm")
                    sys.exit(1)
       
            def actualizacion():
                os.system("clear")
                os.system("tput civis")
                try:
                    ejecutar_comando(["sudo", "apt", "update"], "UPDATE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "parrot-upgrade", "-y"], "UPGRADE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "apt-get", "autoremove", "-y"], "AUTOREMOVE")
                finally:
                    os.system("tput cnorm")
                    print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
       
            if os.geteuid() != 0:
                print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
                sys.exit(1)
        
            actualizacion()
# Ubuntu
    def update_ubuntu():
        if messagebox.askquestion("Update", "¿Desea Actualizar Ubuntu / Mint?") == "yes":
            ventana.destroy()

            def ejecutar_comando(comando, titulo):
                print(f"{AZUL}{titulo}{FIN}\n")
                try:
                    subprocess.run(comando, check=True)
                except subprocess.CalledProcessError:
                    print(f"\n{ROJO}[!] Hubo un error al ejecutar {titulo} {FIN}")
                    os.system("tput cnorm")
                    sys.exit(1)
       
            def actualizacion():
                os.system("clear")
                os.system("tput civis")
                try:
                    ejecutar_comando(["sudo", "apt", "update"], "UPDATE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "apt", "upgrade", "-y"], "UPGRADE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "apt", "autoremove", "-y"], "AUTOREMOVE")
                finally:
                    os.system("tput cnorm")
                    print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
       
            if os.geteuid() != 0:
                print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
                sys.exit(1)
        
            actualizacion()
# Debian
    def update_debian():
        if messagebox.askquestion("Update", "¿Desea Actualizar Debian?") == "yes":
            ventana.destroy()

            def ejecutar_comando(comando, titulo):
                print(f"{AZUL}{titulo}{FIN}\n")
                try:
                    subprocess.run(comando, check=True)
                except subprocess.CalledProcessError:
                    print(f"\n{ROJO}[!] Hubo un error al ejecutar {titulo} {FIN}")
                    os.system("tput cnorm")
                    sys.exit(1)
       
            def actualizacion():
                os.system("clear")
                os.system("tput civis")
                try:
                    ejecutar_comando(["sudo", "apt", "update"], "UPDATE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "apt-get", "dist-upgrade", "-y"], "UPGRADE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "apt-get", "autoremove", "-y"], "AUTOREMOVE")
                finally:
                    os.system("tput cnorm")
                    print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
       
            if os.geteuid() != 0:
                print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
                sys.exit(1)
        
            actualizacion()
# Arch
    def update_arch():
        if messagebox.askquestion("Update", "¿Desea Actualizar Arch Linux?") == "yes":
            ventana.destroy()

            def ejecutar_comando(comando, titulo):
                print(f"{AZUL}{titulo}{FIN}\n")
                try:
                    subprocess.run(comando, check=True)
                except subprocess.CalledProcessError:
                    print(f"\n{ROJO}[!] Hubo un error al ejecutar {titulo} {FIN}")
                    os.system("tput cnorm")
                    sys.exit(1)
       
            def actualizacion():
                os.system("clear")
                os.system("tput civis")
                try:
                    ejecutar_comando(["sudo", "pacman", "-Syu", "--noconfirm"], "UPDATE")
                finally:
                    os.system("tput cnorm")
                    print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
       
            if os.geteuid() != 0:
                print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
                sys.exit(1)
        
            actualizacion()
# Fedora
    def update_fedora():
        if messagebox.askquestion("Update", "¿Desea Actualizar Fedora?") == "yes":
            ventana.destroy()

            def ejecutar_comando(comando, titulo):
                print(f"{AZUL}{titulo}{FIN}\n")
                try:
                    subprocess.run(comando, check=True)
                except subprocess.CalledProcessError:
                    print(f"\n{ROJO}[!] Hubo un error al ejecutar {titulo} {FIN}")
                    os.system("tput cnorm")
                    sys.exit(1)
       
            def actualizacion():
                os.system("clear")
                os.system("tput civis")
                try:
                    ejecutar_comando(["sudo", "dnf", "upgrade", "--refresh", "-y"], "UPGRADE")
                    print("\n" + "-"*30 + "\n")
                    ejecutar_comando(["sudo", "dnf", "autoremove", "-y"], "AUTOREMOVE")
                finally:
                    os.system("tput cnorm")
                    print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
       
            if os.geteuid() != 0:
                print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
                sys.exit(1)
        
            actualizacion()

# ──────────────────────────────────────────────
#  Interfaz gráfica
# ──────────────────────────────────────────────
ventana = Tk()
ventana.title("LinuxUpdate v1.2")
ventana.geometry("400x580") # Un poco más alta para que quepa el texto
ventana.configure(bg=BG_COLOR)

# Variables de control
seleccion = StringVar()
texto_distro = "No detectada" # Variable para mostrar en el Label

# Auto-selección y Detección 
try:
    if os.path.exists("/etc/os-release"):
        with open("/etc/os-release", "r") as f:
            info_distro = f.read().lower()
            
            if "kali" in info_distro:
                seleccion.set("Kali")
                texto_distro = "Kali Linux"
            elif "parrot" in info_distro:
                seleccion.set("Parrot Os")
                texto_distro = "Parrot OS"
            elif "ubuntu" in info_distro or "mint" in info_distro:
                seleccion.set("Ubuntu / Mint")
                texto_distro = "Ubuntu/Mint"
            elif "debian" in info_distro:
                seleccion.set("Debian")
                texto_distro = "Debian"
            elif "arch" in info_distro:
                seleccion.set("Arch")
                texto_distro = "Arch Linux"
            elif "fedora" in info_distro:
                seleccion.set("Fedora")
                texto_distro = "Fedora"
except Exception:
    pass

# Label Distribución
label_distro = Label(ventana, text=f"Distribución: {texto_distro}", font=("Roboto", 12, "bold"), bg=BG_COLOR, fg=FG_COLOR)
label_distro.pack(side="top", anchor="w", pady=(10, 0), padx=15)

def ejecutar_actualizacion():
    distro = seleccion.get()
    
    if distro == "":
        messagebox.showinfo("Error", "Por favor, selecciona su distribución.")
    elif distro == "Kali":
        Update.update_kali()
    elif distro == "Parrot Os":
        Update.update_parrot()
    elif distro == "Ubuntu / Mint":
        Update.update_ubuntu()
    elif distro == "Debian":
        Update.update_debian()
    elif distro == "Arch":
        Update.update_arch()
    elif distro == "Fedora":
        Update.update_fedora()
        
def crear_fila(nombre_distro):
    frame = Frame(ventana, bg=FRAME_COLOR, bd=0)
    frame.pack(padx=20, pady=5, fill="x")
    
    rb = Radiobutton(frame, text=nombre_distro, variable=seleccion, value=nombre_distro, font=("Roboto", 11, "bold"), bg=FRAME_COLOR, fg=FG_COLOR, activebackground=SELECT_COLOR, activeforeground=FG_COLOR, selectcolor=SELECT_COLOR, indicatoron=False, relief="flat", borderwidth=0, padx=15, pady=15, cursor="hand2")
    rb.pack(fill="both", expand=True)
    return frame

# Creación de distribuciones.
crear_fila("Kali")
crear_fila("Parrot Os")
crear_fila("Ubuntu / Mint")
crear_fila("Debian")
crear_fila("Arch")
crear_fila("Fedora")

# Botón de Actualizar
boton_actualizar = Button(ventana, text="ACTUALIZAR", font=("Roboto", 11, "bold"), bg=BTN_GREEN, fg=FG_COLOR, activebackground="#238e23", activeforeground="white", relief="flat", cursor="hand2", command=ejecutar_actualizacion)
boton_actualizar.pack(padx=20, pady=15, fill="x")

# Botones Inferiores (Ayuda y Salir)
frame_acciones = Frame(ventana, bg=BG_COLOR)
frame_acciones.pack(pady=5)
#Salir
Button(frame_acciones, text="Cerrar", width=12, bg=BTN_RED, fg="white", relief="flat", cursor="hand2", command=ventana.destroy).pack(side="left", padx=10)
#Ayuda
Button(frame_acciones, text="Ayuda", width=12, bg=BTN_GRAY, fg="white", relief="flat", cursor="hand2", command=lambda: messagebox.showinfo("Ayuda", f"Se ha detectado {texto_distro}. Si es incorrecto, cambia a tu distribución.")).pack(side="left", padx=10)

# Banner
banner = Label(ventana, text="By: hmam", font=("Roboto", 9, "italic"), bg=BG_COLOR, fg=FG_COLOR)
banner.place(relx=0.02, rely=0.98, anchor="sw")
# Bucle
ventana.mainloop()