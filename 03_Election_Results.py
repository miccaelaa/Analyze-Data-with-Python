import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# number of people who answered Ceballos
total_ceballos = sum([1 for n in survey_responses if n == 'Ceballos'])
print(total_ceballos)

survey_length = float(len(survey_responses))
percentage_ceballos = 100 * total_ceballos / survey_length
print(str(round(percentage_ceballos, 2)) + '%')

# In the real election, 54% of the 10,000 town population voted for Cynthia Ceballos.

possible_surveys = np.random.binomial(survey_length, .54, size=10000) / survey_length

# Plot a histogram of possible_surveys
plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.show()

possible_surveys_length = float(len(possible_surveys))
incorrect_predictions = len(possible_surveys[possible_surveys < .5])
ceballos_loss_surveys = incorrect_predictions / possible_surveys_length
print(ceballos_loss_surveys)

# see what would happen if you had instead surveyed 7,000 people
large_survey_length =  float(7000)
large_survey = np.random.binomial(large_survey_length, .54, size=10000) / large_survey_length

incorrect_predictions = len(large_survey[large_survey < .5])
ceballos_loss_new = incorrect_predictions / large_survey_length
print(ceballos_loss_new)
