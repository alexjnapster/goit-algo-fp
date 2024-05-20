def greedy_algorithm(items, budget):
    items_ratio = [(name, item['calories'] / item['cost']) for name, item in items.items()]
    items_ratio.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    selected_items = []

    for name, ratio in items_ratio:
        if items[name]['cost'] <= budget:
            selected_items.append(name)
            budget -= items[name]['cost']
            total_calories += items[name]['calories']

    return selected_items, total_calories


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100
selected_items, total_calories = greedy_algorithm(items, budget)
print("Selected items:", selected_items)
print("Total calories:", total_calories)

def dynamic_programming(items, budget):
    dp = [0] * (budget + 1)
    item_list = list(items.keys())

    for item_name in item_list:
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        for j in range(budget, cost - 1, -1):
            dp[j] = max(dp[j], dp[j - cost] + calories)

    result = []
    w = budget
    for item_name in reversed(item_list):
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']
        if w >= cost and dp[w] == dp[w - cost] + calories:
            result.append(item_name)
            w -= cost

    return result, dp[budget]

selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("Selected items (DP):", selected_items_dp)
print("Total calories (DP):", total_calories_dp)