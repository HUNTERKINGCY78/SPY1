def main():
    print ("Pilih kategori pelanggaran:")
    print ("1. Penyebaran informasi pribadi")
    print ("2. trolling")
    print ("3. Dekanon")
    print ("4. Tipuan")
    print ("5. pemain")

    choice = input("Введите номер категории: ")

    categories = {
        '1': 'Penyebaran informasi pribadi',
        '2': 'trolling',
        '3': 'Dekanon',
        '4': 'Tipuan',
        '5': 'pemain'
    }

    if choice not in categories:
        print ("Pilihan yang salah.  Coba lagi.")
        return

    print (f"Anda telah memilih: {categories[choice]}")

    user_id = input("Masukkan ID: ")
    username = input("Masukkan nama pengguna: ")
    violation_link = input("Masukkan tautan ke pelanggaran: ")

    message = f"Kategori: {categories[choice]}\n"
    message += f"ID: {user_id}\n"
    message += f"Nama belakang: {username}\n"
    message += f"Tautan ke pelanggaran: {violation_link}"

    email = "abuse@telegram.org"

    print (f"\nDikirim melalui email {email}")
    print (f"Pesan terkirim:\n{message}")

if __name__ == "__main__":
    main()
