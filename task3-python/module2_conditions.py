# 1. Результат периода (прибыль/убыток)
profit = float(input("Введите прибыль за месяц: ")) # Запрос прибыли за месяц

# Проверяю результат периода
if profit > 0:
    print("Прибыль")
elif profit < 0:
    print("Убыток")
else:
    print("Безубыточность")
print() # пустая строка для разделения между модулями

# 2. Категория бизнеса
revenue = float(input("Введите выручку: ")) # Запрос выручки

# Определяю категорию бизнеса
if revenue < 1_000_000:
    print("Микробизнес")
elif revenue < 10_000_000:
    print("Малый")
elif revenue < 100_000_000:
    print("Средний")
else:
    print("Крупный")
print() # пустая строка для разделения между модулями

# 5. Анализ цен
prices = [255, 0, 1, 1_000_000_000_000_000, 3500.2342525265]

for index, price in enumerate(prices, start=1): # Проходим по списку; enumerate() возвращает пары (индекс, значение); start=1 — нумеруем товары с 1, а не с 0
    mark = " ДОРОГО"
    if price > 300:
        mark = " ДОРОГО"
    else:
        mark = "" # пустая пометка

    print(f"Товар {index}: {price} руб.{mark}")
print() # пустая строка для разделения между модулями

# 7. Накопительный взнос
monthly_deposit = float(input("Сколько откладываете каждый месяц: ")) # Ежемесячный взнос
months = int(input("На сколько месяцев: ")) # Количество месяцев

total_money = 0   # накопленная сумма
print("Накопления по месяцам:")

for month in range(1, months + 1):
    total_money = total_money + monthly_deposit # добавляем взнос
    print("Месяц", month, ":", total_money, "руб.")

print() # пустая строка для разделения между модулями

# 8. Доступность товара
budget = float(input("Ваш бюджет (руб.): ")) # Бюджет покупателя

# Список товаров и их цены
products = ["Хлеб", "Молоко", "Сыр", "Колбаса", "Печенье"]
costs = [40, 70, 350, 500, 80]

print("Проверка доступности:")
# Проходим по всем товарам
for i in range(len(products)):
    name = products[i]      # название
    price = costs[i]        # цена
    if budget >= price:
        print(name, "- доступен")
    else:
        # Сколько не хватает
        shortage = price - budget
        print(name, "- не хватает", shortage, "руб.")