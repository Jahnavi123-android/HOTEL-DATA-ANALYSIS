import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.show()
df = pd.read_csv("C:\\Users\\jahna\\OneDrive\\Desktop\\Data analysis\\notes\\ADVANCE PYTHON\\tips.csv")  
print(df.head())
print(df.isnull().sum())
print(df.tail(10))
