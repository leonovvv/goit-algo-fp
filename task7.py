import random
import matplotlib.pyplot as plt

# Function to simulate dice rolls using Monte Carlo method
def monte_carlo_dice_simulation(num_rolls):
    sums_count = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        dice_sum = dice_1 + dice_2
        sums_count[dice_sum] += 1

    probabilities = {key: (value / num_rolls) * 100 for key, value in sums_count.items()}
    return probabilities

# Run the simulation
num_rolls = 100000
simulated_probabilities = monte_carlo_dice_simulation(num_rolls)

# Analytical probabilities
analytical_probabilities = {
    2: 2.78,
    3: 5.56,
    4: 8.33,
    5: 11.11,
    6: 13.89,
    7: 16.67,
    8: 13.89,
    9: 11.11,
    10: 8.33,
    11: 5.56,
    12: 2.78
}

# Plotting the results
labels = list(analytical_probabilities.keys())
simulated_values = [simulated_probabilities[i] for i in labels]
analytical_values = [analytical_probabilities[i] for i in labels]

x = range(len(labels))
plt.figure(figsize=(10, 6))
plt.bar(x, simulated_values, width=0.4, label='Simulated Probabilities (Monte Carlo)', color='skyblue', align='center')
plt.bar([i + 0.4 for i in x], analytical_values, width=0.4, label='Analytical Probabilities', color='lightgreen', align='center')
plt.xlabel('Sum of Two Dice')
plt.ylabel('Probability (%)')
plt.xticks(x, labels)
plt.title('Monte Carlo Simulation vs Analytical Probabilities for Dice Sums')
plt.legend()
plt.grid(axis='y')
plt.show()
