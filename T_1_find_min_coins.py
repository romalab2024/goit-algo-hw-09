def find_min_coins(amount):
    """
    Динамічне програмування для мінімальної кількості монет.
    :param amount: Сума, яку потрібно видати покупцеві.
    :return: Словник із номіналами монет та їх кількістю.
    """
    coins = [50, 25, 10, 5, 2, 1]  # Доступні номінали монет
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Початкова точка
    
    # Масив для відновлення монет
    coin_used = [-1] * (amount + 1)
    
    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    # Відновлення набору монет
    change = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin not in change:
            change[coin] = 0
        change[coin] += 1
        amount -= coin
    
    return change

# Перевірка роботи
print(find_min_coins(113))  # Очікуваний результат: {50: 2, 10: 1, 2: 1, 1: 1}
