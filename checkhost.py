# checkhost.py

import socket
import dns.resolver
import requests
from ipwhois import IPWhois
import os

def ip_ve_dns_bilgisi_getir(domain):
    print(f"\n[✔] Girilen: {domain}")
    
    # IP Adresi
    try:
        ip = socket.gethostbyname(domain)
        print(f"[✔] IP Adresi: {ip}")
    except:
        print("[-] IP alınamadı.")
        return

    # Reverse DNS (PTR)
    try:
        rev_dns = socket.gethostbyaddr(ip)[0]
        print(f"[✔] Reverse DNS: {rev_dns}")
    except:
        print("[-] Reverse DNS bulunamadı.")

    # DNS Kayıtları
    print("[✔] DNS Kayıtları:")
    for record_type in ['A', 'AAAA', 'MX', 'NS', 'TXT', 'CNAME']:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            print(f"  • {record_type}:")
            for rdata in answers:
                print(f"    - {rdata.to_text()}")
        except:
            pass

    # WHOIS - ASN & Ülke Bilgisi
    try:
        obj = IPWhois(ip)
        results = obj.lookup_rdap()
        print(f"[✔] Hosting / ASN: {results['network']['name']}")
        print(f"[✔] Ülke: {results['network']['country']}")
    except:
        print("[-] Whois bilgisi alınamadı.")

    # HTTP Testi
    try:
        r = requests.get(f"http://{domain}", timeout=5)
        print(f"[✔] HTTP Durumu: {r.status_code}")
    except:
        print("[-] HTTP bağlantısı başarısız.")

    # Ping Testi
    print("[✔] Ping testi yapılıyor...")
    ping = os.system(f"ping -c 3 {domain} > /dev/null 2>&1")
    if ping == 0:
        print("[✔] Ping başarılı.")
    else:
        print("[-] Ping başarısız.")


if __name__ == "__main__":
    try:
        hedef = input("🔎 Domain veya IP girin: ").strip()
        if hedef:
            ip_ve_dns_bilgisi_getir(hedef)
        else:
            print("[-] Geçerli bir domain veya IP girilmedi.")
    except KeyboardInterrupt:
        print("\nİşlem iptal edildi.")
