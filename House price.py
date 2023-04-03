import pandas as pd
housing=pd.read_csv("data.csv")
print(housing.describe())


import matplotlib.pyplot as plt
print(housing.hist(bins=50,figsize=(20,15)))
