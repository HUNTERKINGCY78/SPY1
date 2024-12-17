import requests
from pystyle import Colors, Colorate

class HttpWebNumber:
    def __init__(self) -> None:
        self.__check_number_link: str = "https://htmlweb.ru/geo/api.php?json&telcod="
        self.__not_found_text: str = "Информация отсутствует"

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
            user_number = input(Colorate.Horizontal(Colors.green_to_white, '[+] Введите номер телефона (например, +79833170773): ')).strip()
            if user_number:
                print(Colorate.Horizontal(Colors.green_to_white, '[+] Поиск данных...\n'))
                number_data = self.__return_number_data(user_number=user_number)

                if number_data.get("limit", 1) <= 0:
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] К сожалению, вы израсходовали все лимиты'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Всего лимитов: ' + str(number_data.get("limit", self.__not_found_text))))

                elif number_data.get("status_error") or number_data.get("error"):
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Данные не найдены\n'))
                else:
                    country = number_data.get('country', {})
                    capital = number_data.get('capital', {})
                    region = number_data.get('region', {"autocod": self.__not_found_text, "name": self.__not_found_text, "okrug": self.__not_found_text})
                    other = number_data.get('0', {})

                    if country.get("country_code3") == 'UKR':
                        print(Colorate.Horizontal(Colors.green_to_white, '[+] Страна: Украина'))
                    else:
                        print(Colorate.Horizontal(Colors.green_to_white, '[+] Страна: ' + country.get("name", self.__not_found_text) + ', ' + country.get("fullname", self.__not_found_text)))

                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Город: ' + other.get("name", self.__not_found_text)))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Почтовый индекс: ' + str(other.get("post", self.__not_found_text))))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Код валюты: ' + str(country.get("iso", self.__not_found_text))))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Телефонные коды: ' + str(capital.get("telcod", self.__not_found_text))))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Гос. номер региона авто: ' + str(region.get("autocod", self.__not_found_text))))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Оператор: ' + other.get("oper", self.__not_found_text) + ', ' + other.get("oper_brand", self.__not_found_text) + ', ' + other.get("def", self.__not_found_text)))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Местоположение: ' + country.get("name", self.__not_found_text) + ', ' + region.get("name", self.__not_found_text) + ', ' + other.get("name", self.__not_found_text)))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Локация: ' + number_data.get("location", self.__not_found_text)))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Язык общения: ' + country.get("lang", self.__not_found_text).title() + ', ' + country.get("langcod", self.__not_found_text)))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Край/Округ/Область: ' + region.get("name", self.__not_found_text) + ', ' + region.get("okrug", self.__not_found_text)))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Столица: ' + capital.get("name", self.__not_found_text)))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Широта/Долгота: ' + str(other.get("latitude", self.__not_found_text)) + ', ' + str(other.get("longitude", self.__not_found_text))))

                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Проверьте эти ссылки:'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://www.instagram.com/accounts/password/reset - Поиск аккаунта в Instagram'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://api.whatsapp.com/send?phone=' + user_number + '&text=Привет - Поиск номера в WhatsApp'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://facebook.com/login/identify - Поиск аккаунта FaceBook'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://www.linkedin.com/checkpoint/rp/request-password-reset - Поиск аккаунта Linkedin'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://ok.ru/dk?st.cmd=anonymRecoveryStartPhoneLink - Поиск аккаунта OK'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://twitter.com/account/begin_password_reset - Поиск аккаунта Twitter'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://viber://add?number=' + user_number + ' - Поиск номера в Viber'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://skype:' + user_number + '?call - Звонок на номер с Skype'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] https://t.me/' + user_number + ' - Открыть аккаунт в Телеграмме'))
                    print(Colorate.Horizontal(Colors.green_to_white, '[+] tel:' + user_number + ' - Звонок на номер с телефона'))

                    print(Colorate.Horizontal(Colors.green_to_white, '[+] Всего лимитов: ' + str(number_data.get("limit", self.__not_found_text))))

                    input(Colorate.Horizontal(Colors.green_to_white, '[+] Чтобы завершить поиск, нажмите ENTER '))

            else:
                print(Colorate.Horizontal(Colors.green_to_white, '[+] Ошибка, введите номер телефона!\n'))

        except KeyboardInterrupt:
            print('\n[!] Вынужденная остановка работы!\n')

if __name__ == "__main__":
    checker = HttpWebNumber()
    checker.print_number_results()