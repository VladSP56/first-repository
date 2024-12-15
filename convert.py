def currency_converter():
    # Запрос суммы для конвертации
    amount = float(input("Введите сумму для конвертации: "))

    # Изменяем курс в зависимости от суммы
    if amount < 100:
        exchange_rate = 0.8  # курс для суммы меньше 100
    elif 100 <= amount < 500:
        exchange_rate = 0.75  # курс для суммы от 100 до 500
    else:
        exchange_rate = 0.7  # курс для суммы 500 и выше

    # Конвертация суммы
    converted_amount = amount * exchange_rate

    # Вывод результата
    print(f"Сумма {amount} в исходной валюте равна {converted_amount} в целевой валюте по курсу {exchange_rate}.")

if __name__ == "__main__":
    currency_converter()