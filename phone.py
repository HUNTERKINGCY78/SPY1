import os
import glob
import time
import sys

GREEN = "\033[92m"  # Зеленый цвет текста
WHITE = "\033[97m"  # Белый цвет текста
RESET = "\033[0m"   # Сброс цветового оформления

text_formats = ['.csv', '.txt', '.sql', '.xlsx', '.json', '.log']

def slow_print(text, interval=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(interval)

def print_frame(content, title=""):
    width = max(len(line) for line in content.split('\n')) + 8
    slow_print(f"{GREEN}╔═{'═' * (width - 2)}═╗{RESET}\n", interval=0.05)
    if title:
        slow_print(f"{GREEN}║ {title.center(width - 4)} ║{RESET}\n", interval=0.05)
    for line in content.split('\n'):
        slow_print(f"{GREEN}║  {line.center(width - 4)} ║{RESET}\n", interval=0.05)
    slow_print(f"{GREEN}╚═{'═' * (width - 2)}═╝{RESET}\n", interval=0.05)

def dbsearch(db, value):
    found_results = []
    try:
        with open(db, 'r', encoding='utf-8', errors='ignore') as f:
            Fline = f.readline()

        with open(db, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                if value in line:
                    fdata = line.replace(',', ';').replace('\t', '    ').split(';')
                    sdata = Fline.replace(',', ';').replace('\t', '    ').split(';')
                    found_data = []
                    for i in range(len(fdata)):
                        if len(fdata[i]) < 80:
                            if i < len(sdata):
                                key = sdata[i].replace(' ', '')
                                val = fdata[i].strip() if fdata[i].strip() else 'не найден'

                                if key:
                                    found_data.append(('├ ' + GREEN + key + RESET + ': ' + val, '├ ' + key + ': ' + val))

                    found_data = [line for line in found_data if ': не найден' not in line[1]]

                    if found_data:
                        found_data.insert(0, ('╭━━━━━━━━━━━━━━━━━━━━━━━━━', '╭━━━━━━━━━━━━━━━━━━━━━━━━━'))
                        found_results.append(found_data)

    except BaseException as e:
        print(GREEN + '[ + ] Ошибка: ' + str(e) + RESET)
    return found_results

def search_in_base_folder(value):
    start_time = time.time()
    all_found_results = []
    base_directory = 'base'

    db_files = []
    for ext in text_formats:
        db_files.extend(glob.glob(os.path.join(base_directory, '*' + ext)))

    try:
        with open('результаты_поиска.txt', 'w', encoding='utf-8') as f:
            f.write('Поисковой запрос: ' + value + '\n')
            for db in db_files:
                found_results = dbsearch(db, value)

                if found_results:
                    all_found_results.extend(found_results)
                    for result in found_results:
                        for colored_line, plain_line in result:
                            slow_print(colored_line + '\n', interval=0.01)
                            f.write(plain_line + '\n')
                        slow_print('\n', interval=0.01)
                        f.write('\n')

    except Exception as ex:
        print(ex)
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time

        summary_text = f'\n╭━━━━━━━━━━━━━━━━━━━━━━━━━\n' \
                       f'| Всего найдено результатов: {len(all_found_results)}\n' \
                       f'| Затраченное время: {elapsed_time:.2f} секунд\n' \
                       f'╰━━━━━━━━━━━━━━━━━━━━━━━━━\n'

        slow_print(summary_text, interval=0.01)

def main():
    slow_print(f"{GREEN}Введите поисковой запрос: {RESET}\n", interval=0.01)
    search_query = input(f"{WHITE}")

    slow_print(f"{WHITE}🔍 Поиск...\n", interval=0.01)
    search_in_base_folder(search_query)

if __name__ == '__main__':
    main()