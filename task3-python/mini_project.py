# Вариант 1. Калькулятор рентабельности

# Функция для расчёта прибыли и рентабельности
def calculate_profit_and_margin(revenue, costs):
    profit = revenue - costs                     # прибыль = выручка - затраты
    if revenue > 0:
        margin = (profit / revenue) * 100        # рентабельность в %
    else:
        margin = 0.0
    return profit, margin

# Основная часть программы
print("--- Калькулятор рентабельности ---")

# Ввод данных (переменные разных типов: str, float, bool)
company_name = input("Введите название компании: ")          # str
revenue = float(input("Выручка (руб.): "))                   # float
costs = float(input("Затраты (руб.): "))                     # float

print()

# Расчёт
profit, margin = calculate_profit_and_margin(revenue, costs)

# Оценка рентабельности
if margin > 20:
    rating = "высокая"
elif margin >= 10:
    rating = "средняя"
else:
    rating = "низкая"

# Вывод мини-отчёта
print("- Отчёт -")
print(f"Компания: {company_name}")
print(f"Прибыль: {profit} руб.")
print(f"Рентабельность продаж: {margin}%")
print(f"Оценка: {rating}")

# Цикл for (демонстрация: вывод простой линии из символов)
print("Статус:", end=" ")
for _ in range(5):
    print("*", end="")      # звездочки для наглядности
print(" -> " + rating)

print()

# Дополнительная проверка: убыток или прибыль (условие)
if profit > 0:
    print("Компания работает с прибылью.")
elif profit < 0:
    print("Компания убыточна.")
else:
    print("Безубыточность.")
