import os
from pystyle import Colorate, Colors, Center, Write

os.system("clear")


banner = '''
                ⠤⣤⣤⣤⣄⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣠⣤⠤⠤⠴⠶⠶⠶⠶
                 ⢠⣤⣤⡄⣤⣤⣤⠄⣀⠉⣉⣙⠒⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠴⠘⣉⢡⣤⡤⠐⣶⡆⢶⠀⣶⣶⡦
                 ⣄⢻⣿⣧⠻⠇⠋⠀⠋⠀⢘⣿⢳⣦⣌⠳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠞⣡⣴⣧⠻⣄⢸⣿⣿⡟⢁⡻⣸⣿⡿⠁
                 ⠈⠃⠙⢿⣧⣙⠶⣿⣿⡷⢘⣡⣿⣿⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣷⣝⡳⠶⠶⠾⣛⣵⡿⠋⠀⠀
               ⠀⠀⠀⠀⠉⠻⣿⣶⠂⠘⠛⠛⠛⢛⡛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠛⠀⠉⠒⠛⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⢸⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⠀⢻⡁⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⠀⠘⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                 ⠀⠀⠀⠀⠀⠀⠀⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                                

                                     [SPY OSINT INDO 2025]

  ┌─────────────────────────────┐   ┌─────────────────────────────┐   ┌─────────────────────────────┐
  │ 0  •  Pencarian Universal   │   │ 6  •  Setelah menembus SNILS       │   │ 12  •  Setelah menekan CARD       │   
  │ 1  •  Meninju dengan NOMOR      │   │ 7  •  Melalui DISCORD     │   │ 13  •  Menerobos MAC        │   
  │ 2  •  Meninju GEO dengan NOMOR  │   │ 8  •  Menerobos IP          │   │ 14  •  Dengan cara melubangi NPWP        │   
  │ 3  •  Meninju melalui MAIL       │   │ 9  •  Setelah menekan database          │   │ 15  •  Setelah menembus SEGERA       │   
  │ 4  •  Setelah menerobos Telegram    │   │ 10  •  Setelah menembus AVITO      │   │ 16  • Setelah menembus SEGERA        │   
  │ 5  •  Setelah menerobos di VKONTAKTE   │   │ 11  •  Meninju dengan nama        │   │ 17  •  Setelah menembus SEGERA       │  
  └─────────────────────────────┘   └─────────────────────────────┘   └─────────────────────────────┘
  
  ┌─────────────────────────────┐   ┌─────────────────────────────┐   ┌─────────────────────────────┐
  │ 01  •  PEMBONGKARAN TG ACCA         │   │ 04  •  INFORMASI           │   │ 07  •  Kata Anti Larangan        │
  │ 02  •  PEMBONGKARAN THC             │   │ 05  •  by CY78        │   │ 08  •   COOH...             │
  │ 03  •  PENGHANCURAN SESI          │   │ 06  •  EXIT                 │   │ 09  •  COOH...              │
  └─────────────────────────────┘   └─────────────────────────────┘   └─────────────────────────────┘
'''
print (Colorate.Vertical(Colors.green_to_cyan, banner, 2))

choice = Write.Input("[+] Masukkan nomor -> ", Colors.green_to_cyan, interval=0.005)

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
    print ("Dibuat oleh @CY78 PROEJCT, berlangganan salurannya @CY78!")
elif choice == "07":
    os.system("python banvord.py")




