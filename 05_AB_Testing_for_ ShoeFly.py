import codecademylib3
import pandas as pd

#Database
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

# How many views came from each utm_source?
views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views)

# If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.

ad_clicks['is_click'] = ~ ad_clicks.ad_click_timestamp.isnull()
  # ~ is use like a not operator 
print(ad_clicks.head())

# the percent of people who clicked on ads from each utm_source
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click'])\
                              .user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id').reset_index()

clicks_pivot['percent_clicked'] = round(100 * clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False]), 2)

print(clicks_by_source)
print(clicks_pivot)

# Analyzing an A/B Test
num_AB = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(num_AB)

is_click_AB = ad_clicks.groupby(['experimental_group', 'is_click'])\
                .user_id.count().reset_index()\
                .pivot(
                  columns = 'is_click',
                  index = 'experimental_group',
                  values = 'user_id'
                ).reset_index()
  
print(is_click_AB)

# compare experiments A and B
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

a_clicks_pivot = a_clicks.groupby(['is_click', 'day'])\
                         .user_id.count().reset_index()\
                         .pivot(
                           columns = 'is_click',
                           index = 'day',
                           values = 'user_id'
                         ).reset_index()

a_clicks_pivot['percent_clicked'] = round(100 * a_clicks_pivot[True] / (a_clicks_pivot[True] + a_clicks_pivot[False]), 2)

print(a_clicks_pivot)

b_clicks_pivot = b_clicks.groupby(['is_click', 'day'])\
                         .user_id.count().reset_index()\
                         .pivot(
                           columns = 'is_click',
                           index = 'day',
                           values = 'user_id'
                         ).reset_index()

b_clicks_pivot['percent_clicked'] = round(100 * b_clicks_pivot[True] / (b_clicks_pivot[True] + b_clicks_pivot[False]), 2)

print(b_clicks_pivot)
