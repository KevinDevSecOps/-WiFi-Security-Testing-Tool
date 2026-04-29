#!/usr/bin/env python3
"""
Ejemplo de uso de la herramienta de testing WiFi
SOLO PARA USO EDUCATIVO EN REDES PROPIAS
"""

import sys
sys.path.append('..')

from src.utils import check_root, enable_monitor_mode, get_wireless_interfaces
from src.scanner import WiFiScanner
from src.deauth import DeauthAttack
from colorama import Fore, Style

def main():
    # Verificar permisos
    check_root()
    
    # Obtener interfaces
    interfaces = get_wireless_interfaces()
    if not interfaces:
        print(f"{Fore.RED}[!] No se encontraron interfaces wireless")
        return
    
    print(f"{Fore.GREEN}[+] Interfaces disponibles: {', '.join(interfaces)}")
    interface = interfaces[0]
    
    # Activar modo monitor
    if not enable_monitor_mode(interface):
        return
    
    try:
        # Escanear redes
        scanner = WiFiScanner(interface)
        networks = scanner.scan_networks()
        scanner.display_networks()
        
        # Advertencia
        print(f"\n{Fore.RED}{'='*50}")
        print(f"{Fore.RED}⚠️  ADVERTENCIA: SOLO PRUEBA EN TUS PROPIAS REDES")
        print(f"{Fore.RED}{'='*50}\n")
        
        # Ejemplo de ataque (comentado por seguridad)
        if networks and input(f"{Fore.YELLOW}[?] ¿Realizar prueba de deauth? (s/n): ").lower() == 's':
            target_bssid = list(networks.keys())[0]
            print(f"{Fore.YELLOW}[*] Asegúrate de que esta es TU red: {target_bssid}")
            
            if input(f"{Fore.YELLOW}[?] ¿Confirmar? (s/n): ").lower() == 's':
                deauth = DeauthAttack(interface, target_bssid)
                deauth.start_attack(5)  # 5 paquetes por segundo
        
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[*] Operación cancelada")
    finally:
        # Restaurar interfaz
        from src.utils import disable_monitor_mode
        disable_monitor_mode(interface)

if __name__ == "__main__":
    main()