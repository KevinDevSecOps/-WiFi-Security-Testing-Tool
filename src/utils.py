import subprocess
import sys
import os
from colorama import init, Fore, Style

init(autoreset=True)

def check_root():
    """Verifica permisos de administrador"""
    if os.geteuid() != 0:
        print(f"{Fore.RED}[!] Este script requiere permisos de root")
        print(f"{Fore.YELLOW}[*] Ejecuta: sudo python3 {sys.argv[0]}")
        sys.exit(1)

def enable_monitor_mode(interface):
    """Activa modo monitor en la interfaz"""
    try:
        subprocess.run(['ifconfig', interface, 'down'], check=True)
        subprocess.run(['iwconfig', interface, 'mode', 'monitor'], check=True)
        subprocess.run(['ifconfig', interface, 'up'], check=True)
        print(f"{Fore.GREEN}[+] Modo monitor activado en {interface}")
        return True
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[!] Error al activar modo monitor")
        return False

def disable_monitor_mode(interface):
    """Desactiva modo monitor"""
    try:
        subprocess.run(['ifconfig', interface, 'down'], check=True)
        subprocess.run(['iwconfig', interface, 'mode', 'managed'], check=True)
        subprocess.run(['ifconfig', interface, 'up'], check=True)
        print(f"{Fore.GREEN}[+] Modo monitor desactivado en {interface}")
    except subprocess.CalledProcessError:
        print(f"{Fore.RED}[!] Error al desactivar modo monitor")

def get_wireless_interfaces():
    """Obtiene interfaces wireless disponibles"""
    try:
        result = subprocess.run(['iwconfig'], capture_output=True, text=True)
        interfaces = []
        for line in result.stderr.split('\n'):
            if 'IEEE 802.11' in line or 'no wireless extensions' not in line:
                iface = line.split()[0]
                if iface != 'lo':
                    interfaces.append(iface)
        return interfaces
    except:
        return []