# goit-algo-hw-09
My homework theme 9. Greedy algorithms

Завдання: Оптимальна видача решти касовим апаратом
У цьому завданні реалізуємо два алгоритми:

1. Жадібний алгоритм (find_coins_greedy) – видає решту, починаючи з найбільших доступних номіналів.
2. Метод динамічного програмування (find_min_coins) – знаходить мінімальну кількість монет для формування заданої суми.
  Також порівняємо їхню ефективність.

1. Реалізація жадібного алгоритму (find_coins_greedy)
  Ідея:
Жадібний алгоритм працює за принципом вибору найбільшої доступної монети для видачі решти.

  Псевдокод:
 - Почати з найбільшого номіналу.
 - Доки решта не дорівнює 0:
 - Взяти максимальну кількість цієї монети, що не перевищує залишок.
 - Відняти відповідну суму.
 - Перейти до меншого номіналу та повторити.
   
Реалізацію коду дивись у файлі T_1_find_coins_greedy.py

2. Реалізація методу динамічного програмування (find_min_coins)
Ідея:
Цей метод будує масив dp, де dp[i] – мінімальна кількість монет для суми i.

  Псевдокод:
 - Створюємо масив dp розміром amount + 1, заповнюємо ∞, окрім dp[0] = 0.
 - Для кожної суми i від 1 до amount:
 - Перебираємо всі доступні номінали монет.
 - Оновлюємо dp[i], якщо використання поточної монети зменшує кількість необхідних монет.
 - Відновлюємо набір монет, який формує мінімальну кількість.

Реалізацію коду дивись у файлі T_1_find_min_coins.py

3. Порівняння алгоритмів
Аналіз складності (Big-O)
Алгоритм	             Часова складність	   Просторова складність
Жадібний алгоритм	           O(n)	                    O(1)
Динамічне програмування	     O(n * m)	                O(n)
де n – сума, m – кількість доступних номіналів.

Порівняльний аналіз
Критерій	                 Жадібний алгоритм (find_coins_greedy)	                   Динамічне програмування (find_min_coins)
Швидкість	                             Дуже швидкий (O(n))	                                  Повільніший (O(n * m))
Простота	                             Легкий у реалізації	                                  Складніший через dp-масив
Мінімальність	                         Не завжди мінімальна к-сть монет	                      Завжди мінімальна кількість монет
Оптимальність	                         Може не працювати з довільними наборами монет	        Завжди знаходить оптимальне рішення

Чому жадібний алгоритм НЕ завжди оптимальний?
Жадібний алгоритм обирає найбільші доступні монети, але у деяких випадках існують кращі комбінації.
В нашому завданні (монети [50, 25, 10, 5, 2, 1]) жадібний алгоритм працює ідеально, але для довільних наборів монет динамічне програмування буде більш універсальним.

4. Висновки
   
1. Жадібний алгоритм (find_coins_greedy)

 - Найкраще підходить для стандартних валют (наприклад, гривня, євро, долари).
 - Виконується дуже швидко (O(n)).
 - Простий у реалізації.
 - Не завжди дає мінімальну кількість монет (хоча у нашому випадку працює правильно).

2. Динамічне програмування (find_min_coins)

 - Використовується для будь-яких наборів монет.
 - Завжди знаходить найменшу кількість монет.
 - Складність O(n * m), тобто повільніший за жадібний алгоритм.

3. Який алгоритм вибрати?

 - Якщо набір монет стандартний (гривні, євро, долари) – жадібний алгоритм (швидше і простіше).
 - Якщо набір монет нестандартний – динамічне програмування (оптимальне рішення).

Обидва алгоритми працюють правильно, але вибір методу залежить від характеру даних та вимог до точності.

