import os
from pystyle import Colorate, Colors, Center, Write

os.system("clear")


banner = '''
                                              ▄█    █▄    
                                             ███    ███   
                                             ███    ███   
                                            ▄███▄▄▄▄███▄▄ 
                                           ▀▀███▀▀▀▀███▀  
                                             ███    ███   
                                             ███    ███   
                                             ███    █▀    
           @FELIXSOFTOOL                                                   
█████████████████████████████████████████████████████████████████████████████████████████████████████████


  ┌─────────────────────────────┐   ┌─────────────────────────────┐   ┌─────────────────────────────┐
  │ 0  •  Универсальный Поиск   │   │ 6  •  Пробив по СНИЛС       │   │ 12  •  Пробив по CARD       │   
  │ 1  •  Пробив по НОМЕРУ      │   │ 7  •  Пробив по ДИСКОРД     │   │ 13  •  Пробив по MAC        │   
  │ 2  •  Пробив ГЕО по НОМЕРУ  │   │ 8  •  Пробив по IP          │   │ 14  •  Пробив по ИНН        │   
  │ 3  •  Пробив по ПОЧТЕ       │   │ 9  •  Пробив по БД          │   │ 15  •  Пробив по SOON       │   
  │ 4  •  Пробив по Telegram    │   │ 10  •  Пробив по AVITO      │   │ 16  •  Пробив по SOON       │   
  │ 5  •  Пробив по ВКОНТАКТЕ   │   │ 11  •  Пробив по ФИО        │   │ 17  •  Пробив по SOON       │  
  └─────────────────────────────┘   └─────────────────────────────┘   └─────────────────────────────┘
  
  ┌─────────────────────────────┐   ┌─────────────────────────────┐   ┌─────────────────────────────┐
  │ 01  •  СНОС ТГ АККА         │   │ 04  •  ИНФОРМАЦИЯ           │   │ 07  •  Анти Бан ворд        │
  │ 02  •  СНОС ТГК             │   │ 05  •  by @Felix_335        │   │ 08  •  SOON...              │
  │ 03  •  СНОС СЕССИИ          │   │ 06  •  EXIT                 │   │ 09  •  SOON...              │
  └─────────────────────────────┘   └─────────────────────────────┘   └─────────────────────────────┘
'''
print(Colorate.Vertical(Colors.green_to_cyan, banner, 2))

choice = Write.Input("[+] Введите номер -> ", Colors.green_to_cyan, interval=0.005)

if choice == "0":
    os.system("python phone.py")
elif choice == "1":
    os.system("python phone.py")
elif choice == "2":
    os.system("python phone2.py")
elif choice == "3":
    os.system("python phone.py")
elif choice == "4":
    os.system("python phone.py")
elif choice == "5":
    os.system("python phone.py")
elif choice == "6":
    os.system("python phone.py")
elif choice == "7":
    os.system("python phone.py")
elif choice == "8":
    os.system("python ip.py")
elif choice == "9":
    os.system("python phone.py")
elif choice == "10":
    os.system("python phone.py")
elif choice == "11":
    os.system("python phone.py")
elif choice == "12":
    os.system("python phone.py")
elif choice == "13":
    os.system("python mac.py")
elif choice == "14":
    os.system("python phone.py")
elif choice == "03":
    os.system("python session.py")
elif choice == "01":
    os.system("python snos.py")
elif choice == "02":
    os.system("python snos.py")
elif choice == "04":
    print("Создатель @Felix_335, подпишись на его канал @FELIXSOFTOOL ёпта!")
elif choice == "07":
    os.system("python banvord.py")




