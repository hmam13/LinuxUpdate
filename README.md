# LinuxUpdate

AUTOR:
-----------------------------------------------------------
Desarrollado por Hector Arango 
Github: https://github.com/hmam13
Version: 1.2.0

DESCRIPCION:
-----------------------------------------------------------
En esta nueva version, el script autoselecciona tu distribución para solo
presionar el botón de actualizar que está en la parte inferior de la ventana, 
ejecutando los comandos apropiados en la terminal de forma automatica.

LinuxUpdate es una herramienta con interfaz grafica (GUI) diseñada para 
automatizar y simplificar el proceso de actualizacion en distribuciones 
de Linux.

ADVERTENCIAS:
-----------------------------------------------------------
[!] No intente utilizar una opcion que no corresponda a su distribucion actual. 
Esto podria intentar instalar paquetes incompatibles o causar errores en 
su gestor de paquetes.
 
REQUISITOS:
-----------------------------------------------------------
1. Python 3 instalado.
2. Libreria Tkinter (interfaz grafica):
   - En sistemas basados en Debian (Kali/Parrot): sudo apt install python3-tk
   - En sistemas basados en Arch: sudo pacman -S tk
3. Privilegios de superusuario (sudo).

INSTALACION:
-----------------------------------------------------------
apt git clone https://github.com/hmam13/LinuxUpdate

MODO DE USO:
-----------------------------------------------------------
1. Otorgar permisos de ejecucion al archivo:
   chmod +x LinuxUpdate.py

2. Ejecutar el script con sudo (necesario para las actualizaciones):
   sudo ./LinuxUpdate.py
   o
   sudo python3 LinuxUpdate.py

3. La distribución se autoseleccionará en la ventana emergente.
4. Confirmar la actualizacion en el cuadro de dialogo.
5. El proceso se visualizara en la terminal.

DISTRIBUCIONES SOPORTADAS:
-----------------------------------------------------------
- Kali Linux
- Parrot OS
- Arch Linux
- Ubuntu
- Debian
- Fedora
