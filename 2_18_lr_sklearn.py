from sklearn.linear_model import LinearRegression
import pandas as pd 

df = pd.read_csv("bmi_and_life_expectancy.csv")
X = df[["BMI"]]
y = df[["Life expectancy"]]

lr = LinearRegression()
lr.fit(X, y)

print(lr.predict([[21.07931]]))
