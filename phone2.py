import requests
from pystyle import Colors, Colorate

class HttpWebNumber:
    def __init__(self) -> None:
        self.__check_number_link: str = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.__not_found_text: str = "Tidak ada informasi yang tersedia"

    def __return_number_data(self, user_number: str) -> dict:
        try:
            response = requests.get(self.__check_number_link + user_number, headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15"})
            if response.ok:
                return response.json()
            else:
                return {"status_error": True}
        except requests.exceptions.ConnectionError:
            return {"status_error": True}

    def print_number_results(self) -> None:
        try:
            user_number = input(Colorate.Horizontal(Colors.green_to_white, '[+] Masukkan nomor telepon (misalnya, +62): ')).strip()
            if user_number:
                print(Colorate.Horizontal(Colors.green_to_white, '[+] Pencarian Data...\n'))
                number_data = self.__return_number_data(user_number=user_number)

                if number_data.get("limit", 1) <= 0:
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Sayangnya, Anda telah menggunakan semua batasan Anda'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Batasan total: ' + str(number_data.get("limit", self.__not_found_text))))

                elif number_data.get("status_error") or number_data.get("error"):
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Data tidak ditemukan\n'))
                else:
                    country = number_data.get('country', {})
                    capital = number_data.get('capital', {})
                    region = number_data.get('region', {"autocod": self.__not_found_text, "name": self.__not_found_text, "okrug": self.__not_found_text})
                    other = number_data.get('0', {})

                    if country.get("country_code3") == 'UKR':
                        print(Colorate.Horizontal(Colors.green_to_white, '[+] Страна: Украина'))
                    else:
                        print(Colorate.Horizontal(Colors.green_to_white, '[+] Страна: ' + country.get("name", self.__not_found_text) + ', ' + country.get("fullname", self.__not_found_text)))

                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Kota: ' + other.get("name", self.__not_found_text)))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] kode Pos: ' + str(other.get("post", self.__not_found_text))))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Kode mata uang: ' + str(country.get("iso", self.__not_found_text))))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Kode telepon: ' + str(capital.get("telcod", self.__not_found_text))))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Negara nomor wilayah mobil: ' + str(region.get("autocod", self.__not_found_text))))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Operator: ' + other.get("oper", self.__not_found_text) + ', ' + other.get("oper_brand", self.__not_found_text) + ', ' + other.get("def", self.__not_found_text)))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Lokasi: ' + country.get("name", self.__not_found_text) + ', ' + region.get("name", self.__not_found_text) + ', ' + other.get("name", self.__not_found_text)))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Lokasi: ' + number_data.get("location", self.__not_found_text)))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Bahasa komunikasi: ' + country.get("lang", self.__not_found_text).title() + ', ' + country.get("langcod", self.__not_found_text)))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Wilayah/Kabupaten/Wilayah: ' + region.get("name", self.__not_found_text) + ', ' + region.get("okrug", self.__not_found_text)))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Modal: ' + capital.get("name", self.__not_found_text)))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Lintang/Bujur: ' + str(other.get("latitude", self.__not_found_text)) + ', ' + str(other.get("longitude", self.__not_found_text))))

                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Lihat tautan ini:'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://www.instagram.com/accounts/password/reset - Поиск аккаунта в Instagram'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://api.whatsapp.com/send?phone=' + user_number + '&text=Привет - Поиск номера в WhatsApp'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://facebook.com/login/identify - Поиск аккаунта FaceBook'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://www.linkedin.com/checkpoint/rp/request-password-reset - Поиск аккаунта Linkedin'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink - Поиск аккаунта OK'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://twitter.com/account/begin_password_reset - Поиск аккаунта Twitter'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://viber://add?number=' + user_number + ' - Поиск номера в Viber'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://skype:' + user_number + '?call - Звонок на номер с Skype'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] https://t.me/' + user_number + ' - Открыть аккаунт в Телеграмме'))
                    print (Colorate.Horizontal(Colors.green_to_white, '[+] tel:' + user_number + ' - Звонок на номер с телефона'))

                    print (Colorate.Horizontal(Colors.green_to_white, '[+] Batasan total: ' + str(number_data.get("limit", self.__not_found_text))))

                    input(Colorate.Horizontal(Colors.green_to_white, '[+] Untuk mengakhiri pencarian, klik ENTER '))

            else:
                print (Colorate.Horizontal(Colors.green_to_white, '[+] Untuk menyelesaikan pencarian, klik Error, masukkan nomor telepon Anda!\n'))

        except KeyboardInterrupt:
            print ('\n[!] Penghentian kerja paksa!\n')

if __name__ == "__main__":
    checker = HttpWebNumber()
    checker.print_number_results()
