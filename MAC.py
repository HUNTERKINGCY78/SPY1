import requests
import pystyle

def mac_lookup(mac_address):
    api_url = f"https://api.macvendors.com/{mac_address}"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error: {str(e)}"


mac_address = pystyle.Write.Input("[?] Введите Mac-Address -> ", pystyle.Colors.green_to_white, interval=0.005)  
vendor = mac_lookup(mac_address)


pystyle.Write.Print(f"Vendor: {vendor}", pystyle.Colors.green_to_white, interval=0.005)