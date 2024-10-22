# Завдання 7. Використання методу Монте-Карло
# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, 
# і визначає ймовірність кожної можливої суми.
# Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, які випали на обох кубиках. Підрахуйте, 
# скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
# На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
# Таблиця ймовірностей сум при киданні двох кубиків виглядає наступним чином.

# - Програмно реалізовано алгоритм для моделювання кидання двох ігрових кубиків і побудови таблиці сум та їх імовірностей за допомогою методу Монте-Карло.
# - Код виконується та імітує велику кількість кидків кубиків, обчислює суми чисел, які випадають на кубиках, підраховує, 
# скільки разів кожна можлива сума з’являється у процесі симуляції, і визначає ймовірність кожної можливої суми.
# - Створено таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
# - Зроблено висновки щодо правильності розрахунків шляхом порівняння отриманих за допомогою методу Монте-Карло результатів 
# та результатів аналітичних розрахунків. Висновки оформлено у вигляді файлу readme.md фінального завдання.

import random
import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

# Функція для симуляції кидання двох кубиків за допомогою методу Монте-Карло
def monte_carlo_simulation(num_simulations):
    results = {i: 0 for i in range(2, 13)}  # Зберігаємо кількість випадків для кожної можливої суми (від 2 до 12)

    for _ in range(num_simulations):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        total = dice_1 + dice_2
        results[total] += 1

    probabilities = {key: (value / num_simulations) * 100 for key, value in results.items()}
    return probabilities, results

# Симуляція кидання кубиків
num_simulations = 1000000
probabilities, results = monte_carlo_simulation(num_simulations)

# Аналітичні ймовірності
analytical_data = {
    "Сума": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    "Аналітична імовірність": ["2.78% (1/36)", "5.56% (2/36)", "8.33% (3/36)", "11.11% (4/36)", "13.89% (5/36)", "16.67% (6/36)",
                                "13.89% (5/36)", "11.11% (4/36)", "8.33% (3/36)", "5.56% (2/36)", "2.78% (1/36)"]
}
analytical_df = pd.DataFrame(analytical_data)

# Додавання результатів Монте-Карло та відхилення
monte_carlo_probabilities = [f"{prob:.2f}% ({value}/{num_simulations})" for value, prob in zip(results.values(), probabilities.values())]
analytical_probabilities = [2.78, 5.56, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
absolute_deviation = [f"{abs(prob - analytical_probabilities[i]):.2f}%" for i, prob in enumerate(probabilities.values())]

analytical_df["Імовірність Монте-Карло"] = monte_carlo_probabilities
analytical_df["Відхилення"] = absolute_deviation

# Виведення порівняльної таблиці
print("Порівняння результатів симуляції методом Монте-Карло та аналітичних розрахунків:")
print(tabulate(analytical_df, headers='keys', tablefmt='pretty', showindex=False))

# Побудова графіку для порівняння аналітичних і Монте-Карло ймовірностей (лінії)
sums = analytical_data["Сума"]
monte_carlo_values = list(probabilities.values())
plt.figure(figsize=(10, 6))
plt.plot(sums, analytical_probabilities, marker='o', linestyle='-', color='b', label='Аналітична імовірність')
plt.plot(sums, monte_carlo_values, marker='o', linestyle='-', color='r', label='Імовірність Монте-Карло')
plt.xlabel('Сума на кубиках')
plt.ylabel('Ймовірність (%)')
plt.title('Порівняння аналітичної і Монте-Карло ймовірностей для кидання двох кубиків')
plt.legend()
plt.grid(axis='y')
plt.show()

