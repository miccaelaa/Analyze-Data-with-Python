import fetchmaker
import numpy as np
from scipy.stats import binom_test, f_oneway, chi2_contingency
from statsmodels.stats.multicomp import pairwise_tukeyhsd

# rottweiler's tail length
rottweiler_tl = fetchmaker.get_tail_length("rottweiler")
mean_rottweiler_tl = np.mean(rottweiler_tl)
std_rottweiler_tl = np.std(rottweiler_tl)
print(mean_rottweiler_tl)
print(std_rottweiler_tl)

# We want to know if whippets are significantly more or less likely to be a rescue - Binomial test
whippet_rescue = fetchmaker.get_is_rescue('whippet') # 1 = rescue| 0 = not rescue
num_whippet_rescues = np.count_nonzero(whippet_rescue)
num_whippets = np.size(whippet_rescue)
pval = binom_test(num_whippet_rescues, num_whippets, 0.08)
print(pval)

# Compare if the size of the dogs matters - ANOVA test
w = fetchmaker.get_weight('whippet')
t = fetchmaker.get_weight('terrier')
p = fetchmaker.get_weight('pitbull')
pvalue = f_oneway(w, t, p).pvalue
print(pvalue)

# Tukey's Range Test 
values = np.concatenate([w, t, p])
labels = ['whippet'] * len(w) + ['terrier'] * len(t) + ['pitbull'] * len(p) 

test = pairwise_tukeyhsd(values, labels, 0.05)
print(test)

# We want to see if "poodle"s and "shihtzu"s have significantly different color breakdowns -  Chi Square test
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

color_table = [
  [
    np.count_nonzero(poodle_colors == 'black'),
    np.count_nonzero(shihtzu_colors == 'black')
  ],
  [
    np.count_nonzero(poodle_colors == 'brown'),
    np.count_nonzero(shihtzu_colors == 'brown')
  ],
  [
    np.count_nonzero(poodle_colors == 'gold'),
    np.count_nonzero(shihtzu_colors == 'gold')
  ],
  [
    np.count_nonzero(poodle_colors == 'grey'),
    np.count_nonzero(shihtzu_colors == 'grey')
  ],
  [
    np.count_nonzero(poodle_colors == 'white'),
    np.count_nonzero(shihtzu_colors == 'white')
  ]
]

_, color_pval, _, _ = chi2_contingency(color_table)
print(color_pval)
