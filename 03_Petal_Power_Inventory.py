import pandas as pd

inventory = pd.read_csv('inventory.csv')

# The first 10 rows represent data from your Staten Island location.
staten_island = inventory.head(10)
print(staten_island)

# what products are sold at your Staten Island location
product_request = staten_island.product_description

# what types of seeds are sold at the Brooklyn location.
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]

# Add a column to inventory called in_stock which is True if quantity is greater than 0 and False if quantity equals 0

inventory['in_stock'] = inventory.apply(lambda x: True if x.quantity > 0 else False, axis=1)

# Petal Power wants to know how valuable their current inventory is.
inventory['total_value'] = inventory.price * inventory.quantity

# The Marketing department wants a complete description of each product for their catalog
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type, row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory)

