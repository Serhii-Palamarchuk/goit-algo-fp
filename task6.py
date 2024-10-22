# Завдання 6. Жадібні алгоритми та динамічне програмування
# Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
# Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, а значення — це словник з вартістю та калорійністю.
# items = {
#     "pizza": {"cost": 50, "calories": 300},
#     "hamburger": {"cost": 40, "calories": 250},
#     "hot-dog": {"cost": 30, "calories": 200},
#     "pepsi": {"cost": 10, "calories": 100},
#     "cola": {"cost": 15, "calories": 220},
#     "potato": {"cost": 25, "calories": 350}
# }

# Розробіть функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
# Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті.

# Критерій:
# - Програмно реалізовано функцію, яка використовує принцип жадібного алгоритму. Код виконується і повертає назви страв, максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
# - Програмно реалізовано функцію, яка використовує принцип динамічного
# програмування. Код виконується і повертає оптимальний набір страв для максимізації калорійності при заданому бюджеті.

import pandas as pd
from tabulate import tabulate

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items, budget):
    # Сортуємо страви за зменшенням співвідношення калорій/вартість
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_cost = 0
    total_calories = 0
    selected_items = []

    for item, values in sorted_items:
        if total_cost + values['cost'] <= budget:
            selected_items.append(item)
            total_cost += values['cost']
            total_calories += values['calories']

    return selected_items, total_calories


def dynamic_programming(items, budget):
    # Створюємо таблицю для збереження максимальної калорійності
    n = len(items)
    item_list = list(items.keys())
    cost = [items[item]['cost'] for item in item_list]
    calories = [items[item]['calories'] for item in item_list]

    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю динамічного програмування
    for i in range(1, n + 1):
        for w in range(budget + 1):
            if cost[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost[i - 1]] + calories[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Відновлюємо оптимальний набір страв
    w = budget
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(item_list[i - 1])
            w -= cost[i - 1]

    selected_items.reverse()
    return selected_items, dp[n][budget]


# Приклад використання
budget = 100

# Використання жадібного алгоритму
greedy_result, greedy_calories = greedy_algorithm(items, budget)

greedy_data = {
    "Страва": greedy_result,
    "Калорійність": [items[item]['calories'] for item in greedy_result],
    "Вартість": [items[item]['cost'] for item in greedy_result]
}
greedy_df = pd.DataFrame(greedy_data)
greedy_df.loc["Разом"] = greedy_df[['Калорійність', 'Вартість']].sum()
greedy_df.at["Разом", "Страва"] = "РАЗОМ"
print(f"Результат жадібного алгоритму: Калорійність - {greedy_calories}, Вартість - {greedy_df.at["Разом", "Вартість"]}")
print(tabulate(greedy_df, headers='keys', tablefmt='pretty', showindex=False))

# Використання динамічного програмування
dp_result, dp_calories = dynamic_programming(items, budget)

dp_data = {
    "Страва": dp_result,
    "Калорійність": [items[item]['calories'] for item in dp_result],
    "Вартість": [items[item]['cost'] for item in dp_result]
}
dp_df = pd.DataFrame(dp_data)
dp_df.loc["Разом"] = dp_df[['Калорійність', 'Вартість']].sum()
dp_df.at["Разом", "Страва"] = "РАЗОМ"
print(f"\nРезультат динамічного програмування: Калорійність - {dp_calories}, Вартість - {dp_df.at["Разом", "Вартість"]}")
print(tabulate(dp_df, headers='keys', tablefmt='pretty', showindex=False))
