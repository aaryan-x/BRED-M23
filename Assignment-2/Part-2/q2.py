import pandas as pd
import numpy as np

# Loading the given dataset into a Pandas Dataframe
df = pd.read_csv('IRI_dataset.csv')

# Defining the column ranges for each construct from the dataset
fantasy = df.iloc[:, 0:7]
empathic_concern = df.iloc[:, 7:14]
perspective_taking = df.iloc[:, 14:21]
personal_distress = df.iloc[:, 21:28]

# Function to calculate Cronbach's Alpha
def cronbach_alpha(data):
    item_count = data.shape[1]
    variance_sum = data.var().sum()
    total_variance = data.sum(axis=1).var()
    cronbach_alpha = (item_count / (item_count - 1)) * (1 - (variance_sum / total_variance))
    return cronbach_alpha


# Calculating and Printing the value of Cronbach's Alpha for each construct
print(f"Cronbach's Alpha for Perspective Taking: {cronbach_alpha(perspective_taking):.6f}")
print(f"Cronbach's Alpha for Fantasy: {cronbach_alpha(fantasy):.6f}")
print(f"Cronbach's Alpha for Empathic Concern: {cronbach_alpha(empathic_concern):.6f}")
print(f"Cronbach's Alpha for Personal Distress: {cronbach_alpha(personal_distress):.6f}")
