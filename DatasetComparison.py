import pandas as pd
import math

df = pd.read_csv('blood_pressure.csv')
print(df)

def average(list):
    return sum(list)/len(list)

male_bp = df[df['sex'] == 'Male']['blood pressure'].tolist()
female_bp = df[df['sex'] == 'Female']['blood pressure'].tolist()

avg_male_bp = average(male_bp)
avg_female_bp = average(female_bp)

print("Male Average BP: ", avg_male_bp)
print("Female Average BP: ", avg_female_bp)

# Conditional statements to see which group has greatest average
if(avg_male_bp > avg_female_bp):
    print("The males have a bigger average blood pressure than the females!")
elif(avg_male_bp < avg_female_bp):
    print("The females have a bigger average blood pressure than the males!")
else:
    print("No difference!")

