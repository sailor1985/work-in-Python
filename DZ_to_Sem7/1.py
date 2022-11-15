# 1. Создать телефонный справочник с возможностью импорта и экспорта данных в текстовый формат,
# один из перечисленных на ваш выбор. Под форматом понимаем структуру файлов.
# Техническое задание

# Программа реализует в меню следующие действия:
# Добавить новую запись. Данные вводятся руками в консоли.
# Импортировать из файла (указание имени файла)
# экспорт в файл (указание имени файла)
# Поля записи: Фамилия, Имя, Телефон, Описание.
# Данные(новая запись, импорт из файла) добавляются к уже существующим в системе
# (не затирают существующие). Уникальность данных не обязательна.
# Продумать схему model - view - controller - main
# Считать, что поле не может быть пустой строкой
# При считывании файла целостность данных можно не проверять: считать, что все поля записи есть,
# разделитель полей корректен
# Примеры форматов

# Пользовательский формат: в файле на одной строке хранится одна часть записи, пустая строка -
# разделитель.

# Пример

# Фамилия_1

# Имя_1

# Телефон_1

# Описание_1

# Фамилия_2

# Имя_2

# Телефон_2

# Описание_2
# CSV формат: в файле на одной строке хранится все части записи, символ разделитель записей -
# любой, например , или #, главное, чтобы такой символ не попадался в самих записях.
# Каждая новая запись с новой строки. Здесь нельзя использовать модули библиотеки для парсинга
# CSV файлов. Сделайте обработчик файла самостоятельно.

# Пример

# Фамилия_1,Имя_1,Телефон_1,Описание_1    
# Фамилия_2,Имя_2,Телефон_2,Описание_2
# Усложнение(необязательно). Добавить еще и использование формата файлов XML или JSON.
# Можно использовать дополнительные пакеты для их формирования и обработки.

