from scapy.all import *
from colorama import Fore, Style
import time
from rich.console import Console
from rich.table import Table

class WiFiScanner:
    def __init__(self, interface):
        self.interface = interface
        self.networks = {}
        self.console = Console()
    
    def scan_networks(self, timeout=10):
        """Escanea redes WiFi cercanas"""
        print(f"{Fore.YELLOW}[*] Escaneando redes WiFi...")
        
        self.networks = {}
        
        def packet_handler(pkt):
            if pkt.haslayer(Dot11Beacon):
                bssid = pkt[Dot11].addr2
                ssid = pkt[Dot11Elt].info.decode('utf-8', errors='ignore')
                
                try:
                    channel = ord(pkt[Dot11Elt:3].info)
                except:
                    channel = 0
                
                stats = pkt[Dot11Beacon].network_stats()
                
                self.networks[bssid] = {
                    'ssid': ssid if ssid else '<Oculto>',
                    'channel': channel,
                    'signal': stats.get('signal', 0),
                    'encryption': self._get_encryption(pkt)
                }
        
        sniff(iface=self.interface, prn=packet_handler, timeout=timeout)
        return self.networks
    
    def _get_encryption(self, pkt):
        """Determina el tipo de encriptación"""
        cap = pkt.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}")
        
        if 'privacy' in cap:
            if pkt.haslayer(Dot11EltRSN):
                return 'WPA2'
            elif pkt.haslayer(Dot11EltWPA):
                return 'WPA'
            else:
                return 'WEP'
        return 'OPEN'
    
    def display_networks(self):
        """Muestra las redes encontradas"""
        table = Table(title="Redes WiFi Detectadas")
        table.add_column("N°", style="cyan")
        table.add_column("BSSID", style="magenta")
        table.add_column("SSID", style="green")
        table.add_column("Canal", style="blue")
        table.add_column("Señal", style="yellow")
        table.add_column("Seguridad", style="red")
        
        for i, (bssid, net) in enumerate(self.networks.items(), 1):
            table.add_row(
                str(i),
                bssid,
                net['ssid'],
                str(net['channel']),
                f"{net['signal']} dBm",
                net['encryption']
            )
        
        self.console.print(table)