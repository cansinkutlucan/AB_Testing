import itertools
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.stats.api as sms
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
from statsmodels.stats.proportion import proportions_ztest

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.5f' % x)

control = pd.read_excel('VBO_BootCamp_Donem/5.Hafta/ab_testing.xlsx',sheet_name='Control Group')
control.head()

test = pd.read_excel('VBO_BootCamp_Donem/5.Hafta/ab_testing.xlsx',sheet_name='Test Group')
test.head()

# Ortalamaların incelenmesi:
control['Purchase'].mean()  # 550.8940
test['Purchase'].mean()     # 582.1060


# H0: There isn't significant difference between the number of products purchased
# H1: There is ... 

# Assumptions
# 1.Assumption of Normality(Shapiro Wilks)
# H0: Assumption of normal distribution is provided.
# H1: ... isn't provided.

from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu
from statsmodels.stats.proportion import proportions_ztest
# Control
test_stat, pvalue = shapiro(control["Purchase"])
print('test_stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value>0.05. H0 cannot be rejected. Normality assumption was provided for 'control' data set.

# Test
test_stat, pvalue = shapiro(test["Purchase"])
print('test_stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# p-value>0.05. H0 cannot be rejected. Normality assumption was provided for the 'test' data set.

# 2.The Assumption of Homogeneity of Variance(Levene)
# H0: Variances between two groups are homogeneous
# H1: ... aren't homogeneous

test_stat, pvalue = levene(control["Purchase"].dropna(),
                           test["Purchase"].dropna())

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value>0.05. H0 cannot be rejected. Variances are homogeneous.

# Assumptions provided. Independent two-sample t-test will be applied.(Parametric test)

test_stat, pvalue = ttest_ind(control["Purchase"],test["Purchase"],
                              equal_var=True) # varyans homojenliği = True

print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# p-value>0.34. H0 cannot be rejected. There is no statistically significant difference between the number of purchased products.


# Advice to the customer: There is no difference statistically but there are some increase in the number of sales in average bidding.
# You can wait for a while, collect new data and test again
