from pystyle import Colors, Colorate
import requests
import json

def get_ip_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = response.json()
    return data

def get_ip_type(ip_address):
    url = f"https://ipwho.is/{ip_address}"
    response = requests.get(url)
    ip_info = response.json()
    return ip_info

def color_text(text):
    return Colorate.Horizontal(Colors.green_to_white, text)

def ipsearch(ip_address):
    ip_info = get_ip_info(ip_address)
    print (color_text("╔" + "─" * 65 + "╗"))
    print (color_text("◆ INFORMASI UMUM:"))

    if 'ip' in ip_info:
        print (color_text(f"◆ [+] IP-alamat: {ip_info['ip']}"))
        ip_type_info = get_ip_type(ip_address)
    else:
        print (color_text("◆ [-] IP-alamat tidak tersedia"))

    print(color_text(f"◆ [+] Kota: {ip_info.get('city', 'tidak tersedia')}"))
    print(color_text(f"◆ [+] Wilayah: {ip_info.get('region', 'tidak tersedia')}"))

    print (color_text(f"◆ [+] Benua: {ip_type_info['continent']} {ip_type_info['continent_code']}"))
    print (color_text(f"◆ [+] Negara: {ip_type_info['country']} {ip_type_info['country_code']}"))
    print (color_text(f"◆ [+] Kode Pos: {ip_type_info['postal']}"))
    print (color_text(f"◆ [+] Kode Pos Kode Telepon: {ip_type_info['calling_code']}"))
    print (color_text(f"◆ [+] Bahasa: {ip_type_info['borders']}"))
    print (color_text(f"◆ [+] BahasaZona waktu: {ip_info.get('timezone', 'недоступен')}"))

    print (color_text("◆ ГЕОЛОКАЦИЯ:"))
    if 'loc' in ip_info:
        latitude, longitude = ip_info['loc'].split(',')
        print(color_text(f"◆ [+] Koordinat: {ip_info['loc']}"))
        google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"
        yandex_maps_url = f"https://yandex.ru/maps/?ll={longitude},{latitude}&z=10"
        print(color_text(f"◆ [+] Tautan ke Google Maps: {google_maps_url}"))
        print(color_text(f"◆ [+] Tautan ke Yandex Maps: {yandex_maps_url}"))
    else:
        print(color_text("◆ [-] Koordinat tidak tersedia"))

    print (color_text("◆ INFORMASI TEKNIS:"))
    print (color_text(f"◆ [+] Jenis alamat IP: {ip_type_info['type']}"))
    print (color_text(f"◆ [+] Hostname: {ip_info.get('hostname', 'недоступен')}"))
    print (color_text(f"◆ [+] Organisasi: {ip_info.get('org', 'недоступна')}"))

    print (color_text("◆ PENCARIAN IP DI IoT:"))
    shodan_url = f"https://www.shodan.io/search?query={ip_address}"
    censys_url = f"https://censys.io/ipv4/{ip_address}"
    zoomeye_url = f"https://www.zoomeye.org/searchResult?q={ip_address}"
    criminalip_url = f"https://www.criminalip.io/asset/report/{ip_address}"
    virustotal_url = f"https://www.virustotal.com/gui/ip-address/{ip_address}"

    print (color_text(f"◆ [+] Shodan: {shodan_url}"))
    print (color_text(f"◆ [+] Censys: {censys_url}"))
    print (color_text(f"◆ [+] Zoomeye: {zoomeye_url}"))
    print (color_text(f"◆ [+] CriminalIP: {criminalip_url}"))
    print (color_text(f"◆ [+] VirusTotal: {virustotal_url}"))
    print(color_text("╚" + "─" * 65 + "╝"))

if __name__ == "__main__":
    ip_address = input(color_text("Введите айпи адрес: "))  # Added color to the input prompt
    ipsearch(ip_address)
