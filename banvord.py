import pystyle

def transform_text(input_text):
    translit_dict = {
        "а": "@",
        "б": "Б",
        "в": "B",
        "г": "г",
        "д": "д",
        "е": "е",
        "ё": "ё",
        "ж": "ж",
        "з": "3",
        "и": "u",
        "й": "й",
        "к": "K",
        "л": "л",
        "м": "M",
        "н": "H",
        "о": "0",
        "п": "п",
        "р": "P",
        "с": "c",
        "т": "T",
        "у": "y",
        "ф": "ф",
        "х": "X",
        "ц": "ц",
        "ч": "4",
        "ш": "ш",
        "щ": "щ",
        "ъ": "ъ",
        "ы": "ы",
        "ь": "ь",
        "э": "э",
        "ю": "ю",
        "я": "я",
        "А": "A",
        "Б": "6",
        "В": "V",
        "Г": "r",
        "Д": "D",
        "Е": "E",
        "Ё": "Ё",
        "Ж": "Ж",
        "З": "2",
        "И": "I",
        "Й": "Й",
        "К": "K",
        "Л": "Л",
        "М": "M",
        "Н": "H",
        "О": "O",
        "П": "П",
        "Р": "P",
        "С": "C",
        "Т": "T",
        "У": "Y",
        "Ф": "Ф",
        "Х": "X",
        "Ц": "Ц",
        "Ч": "Ч",
        "Ш": "Ш",
        "Щ": "Щ",
        "Ъ": "Ъ",
        "Ы": "bl",
        "Ь": "b",
        "Э": "Э",
        "Ю": "9Y",
        "Я": "9A",
    }
    transformed_text = []
    for char in input_text:
        if char in translit_dict:
            transformed_text.append(translit_dict[char])
        else:
            transformed_text.append(char)
    return "".join(transformed_text)

input_text = pystyle.Write.Input("\n[+] Введите текст -> ", pystyle.Colors.white_to_green, interval=0.005)
transformed_text = transform_text(input_text)
print()
pystyle.Write.Print("[+] Результат -> " + transformed_text + "\n", pystyle.Colors.green_to_white, interval=0.005)