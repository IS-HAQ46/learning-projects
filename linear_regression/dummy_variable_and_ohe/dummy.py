import pandas as pd 
from sklearn import linear_model
df=pd.read_csv("carprices.csv")
df2=pd.get_dummies(df['Car Model']).astype(int)
merged=pd.concat([df,df2],axis='columns')
final=merged.drop(['Car Model','BMW X5'],axis='columns')
reg=linear_model.LinearRegression()
x=final.drop('Sell Price($)',axis='columns')
y=final['Sell Price($)']
reg.fit(x,y)
print(reg.predict([[45000,4,0,1]]))
print(reg.predict([[86000,7,0,0]]))
print(reg.score(x,y))