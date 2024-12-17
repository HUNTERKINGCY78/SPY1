def main():
    print("Выберите категорию нарушения:")
    print("1. Доксинг")
    print("2. Троллинг")
    print("3. Деанон")
    print("4. Мошенничество")
    print("5. Живодер")

    choice = input("Введите номер категории: ")

    categories = {
        '1': 'Доксинг',
        '2': 'Троллинг',
        '3': 'Деанон',
        '4': 'Мошенничество',
        '5': 'Живодер'
    }

    if choice not in categories:
        print("Неверный выбор. Попробуйте снова.")
        return

    print(f"Вы выбрали: {categories[choice]}")

    user_id = input("Введите ID: ")
    username = input("Введите юзернейм: ")
    violation_link = input("Введите ссылку на нарушение: ")

    message = f"Категория: {categories[choice]}\n"
    message += f"ID: {user_id}\n"
    message += f"Юзернейм: {username}\n"
    message += f"Ссылка на нарушение: {violation_link}"

    email = "abuse@telegram.org"

    print(f"\nОтправлено на почту {email}")
    print(f"Отправленное сообщение:\n{message}")

if __name__ == "__main__":
    main()