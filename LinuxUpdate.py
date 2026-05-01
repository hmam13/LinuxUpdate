#!/usr/bin/env python3

"""
Nombre del Script: LinuxUpdate
Autor: Hector Manuel Arango Martin
Github: https://github.com/hmam13
Descripcióon: Herramienta para automatizar la actualización de Linux.
Lenguaje: Python
"""

import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# --- Configuración de Colores de Terminal ---
VERDE = "\033[1;32m"
ROJO = "\033[1;31m"
AZUL = "\033[1;34m"
AMARILLO = "\033[1;33m"
FIN = "\033[0m"

# --- Configuración de Colores de Interfaz (Simulando Dark Mode) ---
BG_COLOR = "#242424"      # Fondo principal
FG_COLOR = "#FFFFFF"      # Texto
FRAME_COLOR = "#2B2B2B"   # Fondo de los contenedores
BTN_GREEN = "#2eb82e"     # Botón actualizar
BTN_RED = "#cc0000"       # Botón cerrar
BTN_GRAY = "#3d3d3d"      # Botón ayuda

# --- Funciones Lógicas ---

# ---- Kali ----
def update_kali_linux():
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
            finally:
                os.system("tput cnorm")
                print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
       
        if os.geteuid() != 0:
            print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
            sys.exit(1)
        
        actualizacion()

# ---- Parrot ----
def update_parrot_os():
    if messagebox.askquestion("Update", "¿Desea Actualizar Parrot Os?") == "yes":
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
            finally:
                os.system("tput cnorm")
                print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
       
        if os.geteuid() != 0:
            print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
            sys.exit(1)
       
        actualizacion()

# ---- Arch ----
def update_arch():
    if messagebox.askquestion("Update", "¿Desea Actualizar Arch?") == "yes":
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
                ejecutar_comando(["sudo", "pacman", "-Syu"], "UPDATE and UPGRADE")
            finally:
                os.system("tput cnorm")
                print(f"\n{VERDE}[+] Proceso completado exitosamente.{FIN}")
        
        if os.geteuid() != 0:
            print(f"{AMARILLO}[!] Este script debe ejecutarse con sudo.{FIN}")
            sys.exit(1)
        
        actualizacion()

def help_info():
    messagebox.showinfo("Modo de Uso", 
        "Seleccione su distribución para actualizar.\n\n"
        "[!] No use una opción que no corresponda a su distribucion, esto puede ocasionar problemas.")

def salir_programa():
    ventana.destroy()

# --- Interfaz Gráfica ---

ventana = tk.Tk()
ventana.title("LinuxUpdate")
ventana.geometry("350x400")
ventana.configure(bg=BG_COLOR)

# --- Widgets ---

# Título Principal
label_titulo = tk.Label(ventana, text="Seleccione su distribución Linux:", font=("Roboto", 12, "bold"), bg=BG_COLOR, fg=FG_COLOR)
label_titulo.pack(pady=(25, 15), padx=20, anchor="w")

# Función auxiliar para crear filas (frames)
def crear_fila(nombre_distro, comando_update):
    
    frame = tk.Frame(ventana, bg=FRAME_COLOR, bd=0)
    frame.pack(padx=20, pady=5, fill="x")
    
    lbl = tk.Label(frame, text=nombre_distro, font=("Roboto", 11), bg=FRAME_COLOR, fg=FG_COLOR)
    lbl.pack(side="left", padx=15, pady=15)
    
    btn = tk.Button(frame, text="Actualizar", width=10, bg=BTN_GREEN, fg="white", activebackground="#238e23", activeforeground="white", relief="flat", cursor="hand2", command=comando_update)
    btn.pack(side="right", padx=15, pady=10)
    return frame

# Contenedores de Distribuciones
crear_fila("Kali Linux", update_kali_linux)
crear_fila("Parrot OS", update_parrot_os)
crear_fila("Arch Linux", update_arch)

# Espaciador
tk.Label(ventana, bg=BG_COLOR).pack()

# Botones Inferiores (Ayuda y Salir)
frame_acciones = tk.Frame(ventana, bg=BG_COLOR)
frame_acciones.pack(pady=5)

boton_ayuda = tk.Button(frame_acciones, text="Ayuda", width=12, bg=BTN_GRAY, fg="white", activebackground="#555555", activeforeground="white", relief="flat", cursor="hand2", command=help_info)
boton_ayuda.pack(side="left", padx=10)

boton_salir = tk.Button(frame_acciones, text="Cerrar", width=12, bg=BTN_RED, fg="white", activebackground="#990000", activeforeground="white", relief="flat", cursor="hand2", command=salir_programa)
boton_salir.pack(side="left", padx=10)

# --- Banner ---

# Usamos place para fijarlo en la esquina sin mover los otros elementos
label_banner = tk.Label(ventana, text="By: hmam", font=("Roboto", 9, "italic"), bg=BG_COLOR, fg="#555555")
label_banner.place(relx=0.02, rely=0.98, anchor="sw")

# Bucle
ventana.mainloop()