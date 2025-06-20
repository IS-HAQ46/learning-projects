import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn import linear_model
import pickle
df=pd.read_csv("canada_per_capita_income.csv")
plt.xlabel("year")
plt.ylabel("prince($)")
plt.scatter(df.year,df.per_capita_income,color="red",marker='+')

reg=linear_model.LinearRegression()
reg.fit(df[['year']],df.per_capita_income)
print(reg.predict([[2010]],))
plt.plot(df.year,reg.predict(df[["year"]]),color='blue')
plt.show()
with open('model_pickle','wb') as f:
    pickle.dump(reg,f)
with open('model_pickle','rb') as f:
    mod1=pickle.load(f)
print(mod1.predict([[2011]]))
import joblib
joblib.dump(reg,'model_joblib')
mod2=joblib.load('model_joblib')
print(mod2.predict([[2013]]))