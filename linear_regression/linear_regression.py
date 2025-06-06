import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model
df=pd.read_csv("canada_per_capita_income.csv")
plt.xlabel("year")
plt.ylabel("prince($)")
plt.scatter(df.year,df.per_capita_income,color="red",marker='+')

reg=linear_model.LinearRegression()
reg.fit(df[['year']],df.per_capita_income)
print(reg.predict([[2010]],))
plt.plot(df.year,reg.predict(df[["year"]]),color='blue')
