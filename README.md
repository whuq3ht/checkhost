# 🛰️ CheckHost.py

Python ile yazılmış, `check-host.net` benzeri bir IP ve domain bilgi alma aracıdır.  
Girilen alan adı (domain) veya IP üzerinden IP adresi, DNS kayıtları, reverse DNS, whois (ASN & ülke) ve HTTP durumu gibi birçok bilgiyi otomatik olarak toplar.

---

## 📦 Özellikler

- 🌐 IP Adresi Tespiti
- 🧠 DNS Kayıtları (A, MX, TXT, NS, CNAME...)
- 🔄 Reverse DNS (PTR)
- 📡 Whois / ASN & Ülke Bilgisi
- ✅ HTTP Durum Kontrolü
- 📶 Basit Ping Testi (istemci taraflı)

---

## 🚀 Kurulum

> Python 3.7+ gereklidir.

Gerekli paketleri kur:

```bash
pip install requests dnspython ipwhois

python CheckHost.py

Ardından gelen prompt’a IP veya domain yaz:
[✔] Girilen: google.com
[✔] IP Adresi: 142.250.190.206
[✔] Reverse DNS: fra24s30-in-f14.1e100.net
[✔] DNS Kayıtları:
  • A:
    - 142.250.190.206
  • NS:
    - ns1.google.com.
    - ns2.google.com.
...
[✔] Hosting / ASN: GOOGLE
[✔] Ülke: US
[✔] HTTP Durumu: 200
[✔] Ping testi yapılıyor...
[✔] Ping başarılı.

📁 Dosya Yapısı
checkhost.py
README.md

❗ Uyarı
Bu script yalnızca eğitimsel ve bilgi edinme amaçlıdır. İzinsiz tarama, sorgulama veya saldırı faaliyetleri için kullanılması yasaktır.

👨‍💻 Geliştiren
ATCKLabs — https://atcklabs.eu
📬 Instagram: @haktan0zturk
🎥 YouTube: @atcklabs
