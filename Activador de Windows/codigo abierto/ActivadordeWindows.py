import subprocess
import winreg
from colorama import init, Fore, Style

init()

comando = "title activador de windows"
start = "start dependencias.bat"

title = subprocess.run(comando, shell=True, capture_output=True, text=True)
color = subprocess.run(start, shell=True, capture_output=True, text=True)

print(color.stdout)
print(title.stdout)


print( Fore.GREEN + Style.BRIGHT + r""" 
      _____                           __                        
   _/ ____\ ______   ____   ____     |  | __  ____ ___.__. ______
   \   __\ \_  __ \_/ __ \_/ __ \    |  |/ / / __ <   |  |/  ___/
    |  |    |  | \/\  ___/\  ___/    |    < \  ___/\___  |\___ \ 
    |__|    |__|    \___  >\___  >   |__|_ \ \___  > ____/____  >
                     \/     \/         \/     \/\/         \/ 

""")

print(Style.RESET_ALL)





print("""

┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃                                                                                     ┃
┃    [1] Windows 10 Home                    [2] Windows 10 Home N                     ┃
┃    [3] Windows 10 Home Single Language    [4] Windows 10 Home Country Specific      ┃
┃    [5] Windows 10 Professional            [6] Windows 10 Professional N             ┃
┃    [7] Windows 10 Enterprise              [8] Windows 10 Enterprise N               ┃
┃    [9] Windows 10 Education               [10] Windows 10 Education N               ┃
┃    [11] Windows 10 Enterprise 2015 LTSB   [12] Windows 10 Enterprise 2015 LTSB N    ┃
┃                                                                                     ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
      
      
""")

print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" ")

windows = float(input("ingresa la versión de windows que usted posee: "))
key = ""


if windows == 1:
    key = "TX9XD-98N7V-6WMQ6-BX7FG-H8Q99"
elif windows == 2:
    key = "3KHY7-WNT83-DGQKR-F7HPR-844BM"
elif windows == 3:
    key = "7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH"
elif windows == 4:
    key = "PVMJN-6DFY6-9CCP6-7BKTT-D3WVR"
elif windows == 5:
    key = "W269N-WFGWX-YVC9B-4J6C9-T83GX"
elif windows == 6:
    key = "MH37W-N47XK-V7XM9-C7227-GCQG9"
elif windows == 7:
    key = "NPPR9-FWDCX-D2C8J-H872K-2YT43"
elif windows == 8:
    key = "DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4"
elif windows == 9:
    key = "NW6C2-QMPVW-D7KKK-3GKT6-VCFB2"
elif windows == 10:
    key = "2WH4N-8QGBV-H22JP-CT43Q-MDWWJ"
elif windows == 11:
    key = "WNMTR-4C88C-JK8YV-HQ7T2-76DF9"
elif windows == 12:
    key = "2F77B-TNFGY-69QQF-B8YKP-D69TJ"
else:
    print("opción no valida")
    exit()


print(" ")
print(f'la key seleccionada es: ' + Fore.RED + Style.BRIGHT + key)
print(Style.RESET_ALL)
print(" ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" ")

print("""
      
      [1] kms.digiboy.ir [2] kms.msguides.com
      
""")

print(" ")

link = float(input("ingresa el medio de activación:"))
activ_link = ""


if link == 1:
    activ_link = "kms.digiboy.ir"
elif link == 2: 
    activ_link = "kms.msguides.com"
else:
    print("opción no valida")
    exit()

print(" ")
print(f'la Url seleccionada es: '+ Fore.RED + Style.BRIGHT + activ_link)
print(Style.RESET_ALL)
print(" ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" ")

print(Fore.GREEN + Style.BRIGHT +'=== Aplicando la Key al sistema ===')
print(Style.RESET_ALL)

print(" ")

comando1 = f'slmgr /ipk {key}'
comando2 = f'slmgr /skms {activ_link}'  
comando3 = "slmgr /ato"

resultado1 = subprocess.run(comando1, shell=True, capture_output=True, text=True)

print(resultado1.stdout)

resultado2 = subprocess.run(comando2, shell=True, capture_output=True, text=True)

print(resultado2.stdout)

resultado3 = subprocess.run(comando3, shell=True, capture_output=True, text=True)

print(resultado3.stdout)

print(" ")
print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(" ")

def check_windows_activation_status():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows NT\CurrentVersion")
        value, _ = winreg.QueryValueEx(key, "DigitalProductId")
        if value:
            print( Fore.GREEN + Style.BRIGHT + "¡Windows está activado!")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + Style.BRIGHT + "Windows no está activado.")
            print(Style.RESET_ALL)
    except Exception as e:
        print( Fore.RED + Style.BRIGHT + "Error al verificar el estado de activación de Windows:", e)
        print(Style.RESET_ALL)


check_windows_activation_status()

print(" ")

print(Fore.YELLOW + Style.BRIGHT + """
      
    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      
      !IMPORTANTE¡

      ➤ En caso de que no se active windows, vuelve intentando seleccionando otra url.

      ➤ Reinicia tu pc para ver los cambios.

      Creditos:

      ➤ Desarrollado por "Plexy-draw"

      ➤ Github: https://github.com/plexydraw

      ➤ Discord: plexydraw

    ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
      
""")

print(Style.RESET_ALL)

print(" ")

input("Presiona Enter para salir...")

exit()



