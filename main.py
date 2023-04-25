import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("workforce.csv")

avgerage_applied = df.groupby('Borough')['Applied for the program'].mean()
print(avgerage_applied)

grouped_data = df.groupby("Borough")
print("possible boroughs are:")
print(grouped_data.groups.keys())

chosen_borough = input("choose a borough: ")

borough_data = grouped_data.get_group(chosen_borough)
max_applicants = borough_data['Applied for the program'].max()
min_applicants = borough_data['Applied for the program'].min()
number_years = borough_data['Year'].nunique()
print("max number of applicants: ", max_applicants)
print("min number of applicants: ", min_applicants)
print("number of years record in the borough: ", number_years)


output_file = input("Enter output file: ")

borough_data.plot.bar(x="Year", y="Applied for the program")
plt.gcf().subplots_adjust(bottom=0.25)
plt.xlabel("Year")
plt.ylabel("Applied for the program")
plt.savefig(output_file)