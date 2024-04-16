#python3 -m pip install pandas 
import pandas
house = pandas.read_csv('house.csv')
print(house)
print(house.head(2))
print(house.describe())