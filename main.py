import pandas
from sklearn.linear_model import LinearRegression
data = pandas.read_csv('iphone_price.csv')
model = LinearRegression()
model.fit(data[['version']], data[['price']])
print(model.predict([[30]]))
# get data then run at regression model then fit the data and u can predict the future


