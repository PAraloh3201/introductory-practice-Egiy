# 1. calculate_profit()
def calculate_profit(revenue, costs):
    # revenue - выручка
    # costs - затраты
    # profit = доходы - расходы
    profit = revenue - costs
    return profit   # возврат полученное значение

# Проверка работы функции с тремя разными парами
print("--- Блок 1 ---")

result1 = calculate_profit(100_000, 70_000)
print(f"Прибыль составляет: {result1}")

result2 = calculate_profit(50_000, 60_000)
print(f"Прибыль составляет: {result2}")

result3 = calculate_profit(200_000, 200_000)
print(f"Прибыль составляет: {result3}")

print() # пустая строка для разделения между блоками

# 3. get_category()
def get_category(revenue):
    # revenue - годовая выручка в рублях
    if revenue < 1_000_000:
        return "Микробизнес"
    elif revenue < 10_000_000:
        return "Малый бизнес"
    elif revenue < 100_000_000:
        return "Средний бизнес"
    else:
        return "Крупный бизнес"

print("--- Блок 2 ---")
# Тест на четырех разных значениях выручки

print("Выручка 500.000 ->", get_category(500_000))
print("Выручка 5.000.000 ->", get_category(5_000_000))
print("Выручка 50.000.000 ->", get_category(50_000_000))
print("Выручка 200.000.000 ->", get_category(200_000_000_000))

print() # пустая строка для разделения между модулями

# 6. currency_convert()
def currency_convert(amount, rate, direction):
    # amount - сумма для конвертации
    # rate - курс
    # direction - направление
    if direction == 'to_usd':
        # перевод рубли в доллары (рубли / курс)
        return amount / rate
    elif direction == 'to_rub':
        # перевод доллары в рубли: (доллары * курс)
        return amount * rate

print("--- Блок 3 ---")

user_amount = float(input("Введите сумму для конвертации: ")) # пользователь вводит сумму для конвертации
user_rate = float(input("Введите курс (руб. за 1 долл.): ")) # пользователь вводит курс
user_direction = input("Введите направление концертации (to_rub / to_usd): ") # пользователь вводит направление конвертации

# Вызов функции
result = currency_convert(user_amount, user_rate, user_direction)

# Проверка результата на ошибку
if result is None:
    print("error: invalid value")
else:
    print(f"Результат конвертации: {result}")

print() # пустая строка для разделения между блоками

# 7. payback_period()
def payback_period(investment, annual_profit):
    # investment - объем инвестиций
    # annual_profit - годовая прибыль
    if annual_profit <= 0:
        return "err"
    else:
        return (investment / annual_profit)

print("--- Блок 4 ---")

# Запрос данных у пользователя
investment_amount = float(input("Введите объём инвестиций: "))
annual_profit_amount = float(input("Введите годовую прибыль: "))

payback = payback_period(investment_amount, annual_profit_amount)

# Проверка результата на ошибку
if payback is not None:
    print(f"Срок окупаемости: {payback} лет")
else:
    print("error: invalid value")

print() # пустая строка для разделения между блоками

# 8. format_invoice_line()
def format_invoice_line(name, quantity, price):
    # name - название
    # quantity - количество
    # price - цена за штуку

    total = quantity * price
    return name + " × " + str(quantity) + " = " + str(total) + " руб."

print("--- Блок 5 ---")
# Тест
print(format_invoice_line("Хлеб", 2, 40))
print(format_invoice_line("Молоко", 3, 70))
print(format_invoice_line("Цистерна нефти", 50, 3_800_000))
