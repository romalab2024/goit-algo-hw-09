def find_coins_greedy(amount):
    """
    Жадібний алгоритм для видачі решти.
    :param amount: Сума, яку потрібно видати покупцеві.
    :return: Словник із кількістю монет кожного номіналу.
    """
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    change = {}  # Словник для збереження результату
    
    for coin in coins:
        if amount >= coin:
            change[coin] = amount // coin  # Визначаємо, скільки разів можна взяти монету
            amount %= coin  # Оновлюємо залишок
    
    return change

# Перевірка роботи
print(find_coins_greedy(113))  # Очікуваний результат: {50: 2, 10: 1, 2: 1, 1: 1}