import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

data = pd.read_csv('./data-mining-trend/avgFeatures.csv')
features = data.drop('RPA market size',axis=1)

featureLocations = {
    'S&P': 0,
    'Low-code': 1,
    'Intangibles': 2,
    'R&D': 3,
    'Revenue': 4,
    'CapEx': 5
}

X_train = features
X_test = features.iloc[-1].values

print(X_test[featureLocations['S&P']])
print(X_test[featureLocations['Low-code']])
#1. próba
X_test[featureLocations['S&P']] = 4137 
X_test[featureLocations['Low-code']] = 26869 

#2.próba: +10
#3.próba: -10
X_test[featureLocations['R&D']] = X_test[featureLocations['R&D']] - X_test[featureLocations['R&D']]*0.2
X_test[featureLocations['CapEx']] = X_test[featureLocations['CapEx']] - X_test[featureLocations['CapEx']]*0.2

X_test[featureLocations['Revenue']] = X_test[featureLocations['Revenue']] - X_test[featureLocations['Revenue']]*0.2
#4.próba: +10
#5.próba: -10

#X_test[featureLocations['Intangibles']] = X_test[featureLocations['Intangibles']] + X_test[featureLocations['Intangibles']]*0.1
X_test = X_test.reshape(1, -1) 
y_train = data['RPA market size']
y_test = np.array([data.iloc[-1,-1]])  

lasso = Lasso(alpha=20)

lasso.fit(X_train, y_train)

y_pred = np.array([lasso.predict(X_test)])
print('Predicted value: '+ str(y_pred))
print('Forecasted value: '+ str(y_test))

mse = mean_squared_error(y_test, y_pred)
print("Mean squared error:", mse)

coef = pd.Series(lasso.coef_, index=X_train.columns)
print("Selected features:\n", coef[coef != 0])
