
def correct_input():
    while True:   #Проверка коорректности ввода согласия на начало жеребьевки
        answer = input("ДА/НЕТ?: ")
        if answer == "":
            print("\nПустой ввод. Повторите снова:" ) 
            continue
        elif answer.isdigit() or not answer.lower() == "да" :
            print("\nОшибка. Введите ДА или НЕТ. Попробуйте еще раз:" ) 
            continue
        elif answer.lower() == "нет":
            print("\nОтступать некуда, позади Москва. Вводи скорее ДА!" ) 
            continue
        else:
            break
    print("\nУРА!!!!!  ПОЕХАЛИ!!!!!!\n")