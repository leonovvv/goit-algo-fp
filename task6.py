items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

# Greedy Algorithm
def greedy_algorithm(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]['calories'] / x[1]['cost'], reverse=True)
    total_calories = 0
    selected_items = {}
    
    for item, details in sorted_items:
        if budget >= details['cost']:
            num_items = budget // details['cost']
            selected_items[item] = num_items
            total_calories += num_items * details['calories']
            budget -= num_items * details['cost']
    
    return selected_items, total_calories

# Dynamic Programming Algorithm
def dynamic_programming(items, budget):
    n = len(items)
    item_list = list(items.items())
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        item_name, item_details = item_list[i - 1]
        cost = item_details['cost']
        calories = item_details['calories']
        
        for w in range(budget + 1):
            if cost <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - cost] + calories)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtracking to find selected items
    w = budget
    selected_items = {}
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            item_name, item_details = item_list[i - 1]
            cost = item_details['cost']
            if item_name in selected_items:
                selected_items[item_name] += 1
            else:
                selected_items[item_name] = 1
            w -= cost
    
    total_calories = dp[n][budget]
    return selected_items, total_calories

# Example usage
budget = 100

greedy_result = greedy_algorithm(items, budget)
print("Greedy Algorithm Result:")
print("Selected Items:", greedy_result[0])
print("Total Calories:", greedy_result[1])

dp_result = dynamic_programming(items, budget)
print("\nDynamic Programming Result:")
print("Selected Items:", dp_result[0])
print("Total Calories:", dp_result[1])
