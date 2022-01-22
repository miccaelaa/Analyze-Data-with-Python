import codecademylib3
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# Inspect DataFrames
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# Combine visits and cart using a left merge.
visits_cart = pd.merge(visits, cart, how='left')
visits_cart_rows = len(visits_cart)
print(visits_cart.head())

# What percent of users ended up not placing a t-shirt in their cart?
cart_time_null = len(visits_cart[visits_cart.cart_time.isnull()])
print(cart_time_null)
cart_percent_null = 100 * float(cart_time_null) / visits_cart_rows
print(f'{cart_percent_null} % of the users ended up not placing a t-shirt in their cart.')

# Combine cart and checkout using a left merge.
cart_checkout = pd.merge(cart, checkout, how='left')
cart_checkout_rows = len(cart_checkout)
print(cart_checkout.head())

# What percentage of users put items in their cart, but did not proceed to checkout?
checkout_time_null = len(cart_checkout[cart_checkout.checkout_time.isnull()])
c_percent_null = round(100 * float(checkout_time_null) / cart_checkout_rows, 2)
print(f'{c_percent_null} % of the users put items in their cart, but did not proceed to checkout.')

# What percentage of users proceeded to checkout, but did not purchase a t-shirt?
checkout_purchase = pd.merge(checkout, purchase, how='left')
checkout_purchase_rows = len(checkout_purchase)
print(checkout_purchase.head())

purchase_time_null = len(checkout_purchase[checkout_purchase.purchase_time.isnull()])

percent_c_p = round(100 * float(purchase_time_null) / checkout_purchase_rows, 2)
print(f'{percent_c_p} % of users proceeded to checkout, but did not purchase a t-shirt')

# Merge all the dataframes
all_data = visits\
           .merge(cart, how='left')\
           .merge(checkout, how='left')\
           .merge(purchase, how='left')\

print(all_data.head())
all_data_rows = len(all_data)

# Average Time to Purchase
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

print(all_data.time_to_purchase)
print(all_data.time_to_purchase.mean())
