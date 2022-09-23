import csv
from operator import itemgetter

count_rows = 0 # количество записей в файле
count_longrows = 0 # количество записей в файле с названием длиннее 30 символов

new_file = open('Links.txt', 'w')

with open('books.csv', 'r') as csvfile:
    table = list(csv.reader(csvfile, delimiter=';'))
    title = table.pop(0)
    print('Количество записей: ', len(table))

    for row in table:
        if len(row[1]) > 30:
            count_longrows += 1
    print('Количество названий длиннее 30 символов: ', count_longrows)

    search = input("I'm searching for ") # поиск книги по автору
    flag = False
    for row in table:
        index_first = (row[3].lower()).find(search.lower())
        index_second = (row[4].lower()).find(search.lower())
        if index_first != -1 and int(row[6][6:10]) >= 2018:  # ограничение: от 2018 года
            flag = True
            print(row)
        elif index_second != -1 and int(row[6][6:10]) >= 2018:
            flag = True
            print(row)
    if flag is False:
        print('Nothing has been found, sorry')

    # генератор библиографических ссылок
    for i in range(40, 60):
        new_file.write(str(i - 39) + '. ' + table[i][3] + '. ' + table[i][1] + ' - ' + table[i][6][6:10] + '\n')

    # Конец основной части лабораторной работы
    # Начало допзаданий

    # Выдать перечень всех тегов без повторений
    tags = []  # список, где хранятся неповторяющиеся теги
    for row in table:
        row_tags = (str(row[-1]).split('#'))  #приводим теги к единому виду
        row_tags.remove('')
        for tag in row_tags:
            if tag[0] == ' ':
                tag = tag[1:]

            if tag not in tags:
                tags.append(tag)  # записываем в список новые теги
    tags.sort()
    new_file.write('\n Список всех тегов без повторений: \n')
    for tag in tags:
        new_file.write(tag + '\n')

    # Самые популярные 20 книг
    new_file.write('\n 20 самых популярных книг: \n')
    for row in table:
        row[8] = int(row[8])
    sorted_table = sorted(table, key=itemgetter(8), reverse=True)[:25]
    for i in range(1,21):
        new_file.write(str(i) + '. ' + str(sorted_table[i][3]) + '. ' + str(sorted_table[i][1])
        + ' - ' + str(sorted_table[i][6][6:10]) + '  Количество выдач: ' + str(sorted_table[i][8]) + '\n')

new_file.close()