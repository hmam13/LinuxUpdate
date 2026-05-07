=========================================
      ¡BIENVENIDO A TU ACTUALIZADOR!
=========================================

# LinuxUpdate

-----------------------------------------------------------
AUTOR:
-----------------------------------------------------------
Desarrollado por Hector Arango (hmam)
Github: https://github.com/hmam13
Version: 1.0

-----------------------------------------------------------
ADVERTENCIAS:
-----------------------------------------------------------
[!] No intente utilizar una opcion que no corresponda a su distribucion actual. 
Esto podria intentar instalar paquetes incompatibles o causar errores en 
su gestor de paquetes.

-----------------------------------------------------------
DESCRIPCION:
-----------------------------------------------------------
LinuxUpdate es una herramienta con interfaz grafica (GUI) diseñada para 
automatizar y simplificar el proceso de actualizacion en distribuciones 
de Linux basadas en Kali, Parrot OS y Arch Linux. 

El script utiliza una interfaz moderna en "Modo Oscuro" para que el usuario 
pueda actualizar su sistema con un solo clic, ejecutando los comandos 
apropiados en la terminal de forma automatica.

-----------------------------------------------------------
REQUISITOS:
-----------------------------------------------------------
1. Python 3 instalado.
2. Libreria Tkinter (interfaz grafica):
   - En sistemas basados en Debian (Kali/Parrot): sudo apt install python3-tk
   - En sistemas basados en Arch: sudo pacman -S tk
3. Privilegios de superusuario (sudo).

-----------------------------------------------------------
INSTALACION:
-----------------------------------------------------------
Descarga o clona el script.

-----------------------------------------------------------
MODO DE USO:
-----------------------------------------------------------
1. Otorgar permisos de ejecucion al archivo:
   chmod +x LinuxUpdate.py

2. Ejecutar el script con sudo (necesario para las actualizaciones):
   sudo ./LinuxUpdate.py
   o
   sudo python3 LinuxUpdate.py

3. Seleccionar la distribucion correspondiente en la ventana emergente.
4. Confirmar la actualizacion en el cuadro de dialogo.
5. El proceso se visualizara en la terminal.

-----------------------------------------------------------
DISTRIBUCIONES SOPORTADAS:
-----------------------------------------------------------
- Kali Linux
- Parrot OS
- Arch Linux 
