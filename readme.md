# Симуляція кидання кубиків та аналіз ймовірностей

## Огляд
Цей проект симулює кидання двох кубиків велику кількість разів (1,000,000) та обчислює ймовірності кожної можливої суми (від 2 до 12). Результати потім порівнюються з аналітичними ймовірностями.

## Аналітичні ймовірності
Теоретичні ймовірності кожної можливої суми при киданні двох шестигранних кубиків наступні:
- Сума 2: 2.78% (1/36)
- Сума 3: 5.56% (2/36)
- Сума 4: 8.33% (3/36)
- Сума 5: 11.11% (4/36)
- Сума 6: 13.89% (5/36)
- Сума 7: 16.67% (6/36)
- Сума 8: 13.89% (5/36)
- Сума 9: 11.11% (4/36)
- Сума 10: 8.33% (3/36)
- Сума 11: 5.56% (2/36)
- Сума 12: 2.78% (1/36)


## Висновок
Симульовані ймовірності тісно відповідають аналітичним ймовірностям, що демонструє точність методу Монте-Карло для такого типу аналізу ймовірностей. Незначні варіації зумовлені властивою випадковістю процесу симуляції, але при великій кількості симуляцій (1,000,000) ці варіації мінімальні.

Графік, включений в симуляцію, показує це порівняння візуально, підкреслюючи висновок, що метод Монте-Карло надає надійне наближення до справжніх ймовірностей.

