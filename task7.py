import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

num_simulations = 1000000

dice_1 = np.random.randint(1, 7, num_simulations)
dice_2 = np.random.randint(1, 7, num_simulations)
sums = dice_1 + dice_2

sum_counts = pd.Series(sums).value_counts().sort_index()
probabilities = sum_counts / num_simulations * 100

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

comparison_df = pd.DataFrame({
    'Simulated Probability (%)': probabilities,
    'Analytical Probability (%)': pd.Series(analytical_probabilities)
}).fillna(0)

import ace_tools as tools; tools.display_dataframe_to_user(name="Comparison of Simulated and Analytical Probabilities", dataframe=comparison_df)

plt.figure(figsize=(10, 6))
plt.plot(comparison_df.index, comparison_df['Simulated Probability (%)'], marker='o', label='Simulated')
plt.plot(comparison_df.index, comparison_df['Analytical Probability (%)'], marker='x', label='Analytical')
plt.xlabel('Sum')
plt.ylabel('Probability (%)')
plt.title('Comparison of Simulated and Analytical Probabilities for Dice Sums')
plt.legend()
plt.grid(True)
plt.show()