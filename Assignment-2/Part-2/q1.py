import pandas as pd
from sklearn.metrics import cohen_kappa_score

# Loading the given dataset into a Pandas Dataframe
df = pd.read_csv('dataset1.csv')

# Calculating Cohen's Kappa score for each pair of raters from the dataset
AB_kappa_score = cohen_kappa_score(df['Rater_A_Score'], df['Rater_B_Score'])
BC_kappa_score = cohen_kappa_score(df['Rater_B_Score'], df['Rater_C_Score'])
AC_kappa_score = cohen_kappa_score(df['Rater_A_Score'], df['Rater_C_Score'])

#Printing the results
print(f"Cohen's Kappa score for the pair AB: {AB_kappa_score:.4f}")
print(f"Cohen's Kappa score for the pair BC: {BC_kappa_score:.4f}")
print(f"Cohen's Kappa score for the pair AC: {AC_kappa_score:.4f}")
