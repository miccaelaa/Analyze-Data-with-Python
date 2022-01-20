import numpy as np

# Columns = ingredients(flour, sugar, eggs, milk, butter) 
# Rows = recipes

recipes = np.genfromtxt('recipes.csv', delimiter=',')
print(recipes)

eggs = recipes[:, 2]
print(eggs)

# Which recipes require exactly 1 egg?
one_egg = eggs == 1
print(one_egg)

#  2 batches of cupcakes and 1 batch of cookies
cupcakes = recipes[0,:]
cookies = recipes[2,:]

double_batch = cupcakes * 2

grocery_list = double_batch + cookies
