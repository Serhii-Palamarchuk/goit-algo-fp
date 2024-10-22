# Завдання 1. Структури даних. Сортування. Робота з однозв'язним списком
# Для реалізації однозв'язного списку (приклад реалізації можна взяти з конспекту) необхідно:
    # написати функцію, яка реалізує реверсування однозв'язного списку, змінюючи посилання між вузлами;
    # розробити алгоритм сортування для однозв'язного списку, наприклад, сортування вставками або злиттям;
    # написати функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список.


# - Реалізовано функцію реверсування однозв'язного списку, яка змінює посилання між вузлами. Код виконується.
# - Програмно реалізовано алгоритм сортування (функцію) для однозв'язного списку. Код виконується.
# - Реалізовано функцію, що об'єднує два відсортовані однозв'язні списки в один відсортований список. Код виконується.


class Node:
    def __init__(self, data):
        # Ініціалізація вузла зі значенням даних
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Ініціалізація порожнього однозв'язного списку
        self.head = None

    def append(self, data):
        # Додавання нового елементу в кінець списку
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        # Виведення елементів списку
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Функція для реверсування однозв'язного списку
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  # Зберігаємо посилання на наступний вузол
            current.next = prev  # Змінюємо посилання на попередній вузол
            prev = current  # Зміщуємо prev на поточний вузол
            current = next_node  # Зміщуємо current на наступний вузол
        self.head = prev  # Оновлюємо голову списку

    # Функція для сортування однозв'язного списку за допомогою сортування злиттям
    def merge_sort(self):
        if self.head is None or self.head.next is None:
            return self.head

        # Знаходимо середину списку
        middle = self.get_middle(self.head)
        next_to_middle = middle.next

        # Розділяємо список на дві частини
        middle.next = None

        left = LinkedList()
        right = LinkedList()

        left.head = self.head
        right.head = next_to_middle

        # Рекурсивно сортуємо кожну частину
        left_sorted = left.merge_sort()
        right_sorted = right.merge_sort()

        # Об'єднуємо відсортовані частини
        sorted_list = self.sorted_merge(left_sorted, right_sorted)
        self.head = sorted_list
        return self.head

    def get_middle(self, head):
        # Знаходження середнього елементу списку
        if head is None:
            return head

        slow = head
        fast = head

        # Використовуємо два покажчики: швидкий та повільний
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def sorted_merge(self, left, right):
        # Об'єднання двох відсортованих списків
        if left is None:
            return right
        if right is None:
            return left

        # Порівнюємо значення та будуємо об'єднаний список
        if left.data <= right.data:
            result = left
            result.next = self.sorted_merge(left.next, right)
        else:
            result = right
            result.next = self.sorted_merge(left, right.next)

        return result

    # Функція для об'єднання двох відсортованих списків
    def merge_two_sorted_lists(self, l1, l2):
        dummy = Node(0)  # Створюємо тимчасовий вузол
        tail = dummy

        # Поки обидва списки не порожні, додаємо менший елемент до результату
        while l1 and l2:
            if l1.data <= l2.data:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Додаємо залишки елементів одного з двох списків
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2

        return dummy.next

# Тестування реалізації
ll = LinkedList()
ll.append(3)
ll.append(1)
ll.append(4)
ll.append(2)

print("Оригінальний список:")
ll.print_list()

# Реверсування однозв'язного списку
ll.reverse()
print("Реверсований список:")
ll.print_list()

# Сортування однозв'язного списку
ll.head = ll.merge_sort()
print("Відсортований список:")
ll.print_list()

# Об'єднання двох відсортованих однозв'язних списків
ll1 = LinkedList()
ll1.append(1)
ll1.append(3)
ll1.append(5)

ll2 = LinkedList()
ll2.append(2)
ll2.append(4)
ll2.append(6)

merged_list = LinkedList()
merged_list.head = ll.merge_two_sorted_lists(ll1.head, ll2.head)
print("Об'єднаний відсортований список:")
merged_list.print_list()
