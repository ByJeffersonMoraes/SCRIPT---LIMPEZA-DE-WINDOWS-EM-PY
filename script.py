import os
import shutil
import subprocess

def limpar_pasta(caminho):
    try:
        if os.path.isfile(caminho):
            os.remove(caminho)
            return

        if os.path.exists(caminho):
            for item in os.listdir(caminho):
                item_path = os.path.join(caminho, item)

                try:
                    if os.path.isfile(item_path) or os.path.islink(item_path):
                        os.unlink(item_path)

                    elif os.path.isdir(item_path):
                        shutil.rmtree(item_path, ignore_errors=True)

                except:
                    pass
    except:
        pass


def limpar_lista(pastas):
    for pasta in pastas:
        caminho = os.path.expandvars(pasta)

        if os.path.exists(caminho):
            print("Limpando:", caminho)
            limpar_pasta(caminho)


pastas = [

# TEMP
r"C:\Windows\Temp",
r"%TEMP%",
r"%TMP%",

# PREFETCH
r"C:\Windows\Prefetch",

# WINDOWS UPDATE
r"C:\Windows\SoftwareDistribution\Download",
r"C:\Windows\SoftwareDistribution\DeliveryOptimization",

# LOGS
r"C:\Windows\Logs",
r"C:\Windows\System32\LogFiles",
r"C:\Windows\Panther",

# CRASH
r"C:\Windows\Minidump",
r"C:\Windows\MEMORY.DMP",

# DRIVER CACHE
r"C:\Windows\System32\DriverStore\Temp",

# DIRECTX
r"%LOCALAPPDATA%\D3DSCache",

# WINDOWS EXPLORER CACHE
r"%LOCALAPPDATA%\Microsoft\Windows\Explorer",

# INTERNET CACHE
r"%LOCALAPPDATA%\Microsoft\Windows\INetCache",

# EDGE CACHE
r"%LOCALAPPDATA%\Microsoft\Edge\User Data\Default\Cache",

# CHROME CACHE
r"%LOCALAPPDATA%\Google\Chrome\User Data\Default\Cache",

# FIREFOX CACHE
r"%LOCALAPPDATA%\Mozilla\Firefox\Profiles",

# MICROSOFT STORE
r"%LOCALAPPDATA%\Packages",

# ICON CACHE
r"%LOCALAPPDATA%\IconCache.db",

# THUMBNAILS
r"%LOCALAPPDATA%\Microsoft\Windows\Explorer\thumbcache",

# ERROR REPORT
r"C:\ProgramData\Microsoft\Windows\WER",

# DELIVERY OPTIMIZATION
r"C:\ProgramData\Microsoft\Windows\DeliveryOptimization",

# WINDOWS DEFENDER CACHE
r"C:\ProgramData\Microsoft\Windows Defender\Scans\History",

# TEMP INSTALLERS
r"C:\Windows\Installer",

# GAME CACHE
r"%LOCALAPPDATA%\Temp",

# DIAGNOSTIC
r"C:\Windows\Diagnostics",

# OLD UPDATE LOGS
r"C:\Windows\Logs\CBS",

]

def limpar_lixeira():
    subprocess.run("rd /s /q C:\\$Recycle.Bin", shell=True)

def limpar_dns():
    subprocess.run("ipconfig /flushdns", shell=True)

def reset_windows_update():

    subprocess.run("net stop wuauserv", shell=True)
    subprocess.run("net stop bits", shell=True)

    subprocess.run("net start wuauserv", shell=True)
    subprocess.run("net start bits", shell=True)

def limpar_store():
    subprocess.run("wsreset.exe", shell=True)

def limpeza_disco():
    subprocess.run("cleanmgr /verylowdisk", shell=True)

def otimizar_disco():
    subprocess.run("defrag C: /O", shell=True)

def main():

    print("===================================")
    print(" WEVEN.INVENTORY - LIMPEZA DE SISTEMA ")
    print("===================================")

    limpar_lista(pastas)

    print("Limpando lixeira...")
    limpar_lixeira()

    print("Limpando DNS...")
    limpar_dns()

    print("Reset Windows Update...")
    reset_windows_update()

    print("Reset Microsoft Store...")
    limpar_store()

    print("Limpeza de Disco...")
    limpeza_disco()

    print("Otimização do Disco...")
    otimizar_disco()

    print("===================================")
    print(" WEVEN.INVENTORY - LIMPEZA DE SISTEMA COMPLETA FINALIZADA ")
    print("===================================")

if __name__ == "__main__":
    main()

    # Direitos reservados para Jefferson Moraes #


