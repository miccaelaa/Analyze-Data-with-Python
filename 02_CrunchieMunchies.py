import numpy as np

# Reported calorie amounts for different cereal brands.
calorie_stats = np.genfromtxt('cereal.csv', delimiter=",")

average_calories = np.mean(calorie_stats)
print(average_calories)

calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

median_calories = np.median(calorie_stats)
print(median_calories)

# Find the lowest percentile that is greater than 60 calories.
print(np.percentile(calorie_stats, 25))
print(np.percentile(calorie_stats, 12))
print(np.percentile(calorie_stats, 6))
print(np.percentile(calorie_stats, 4))

nth_percentile = 4

# calculate the percentage of cereals that have more than 60 calories per serving.

more_calories = 100 - nth_percentile
print(more_calories)

# Standar deviation
calorie_std = np.std(calorie_stats)
print(calorie_std)
