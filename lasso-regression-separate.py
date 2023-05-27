import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error

data = pd.read_csv('./data-mining-trend/features.csv')
features = data.drop('RPA market size',axis=1)

RnDpositions = [2,6,10,14,18]

X_train = features
X_test = features.iloc[-1].values

X_test = X_test.reshape(1, -1) 
y_train = data['RPA market size']
y_test = np.array([data.iloc[-1,-1]])  

lasso = Lasso(alpha=0.1)

lasso.fit(X_train, y_train)

y_pred = np.array([lasso.predict(X_test)])
print('Predicted value: '+ str(y_pred))
print('Forecasted value: '+ str(y_test))

mse = mean_squared_error(y_test, y_pred)
print("Mean squared error:", mse)

coef = pd.Series(lasso.coef_, index=X_train.columns)
print("Selected features:\n", coef[coef != 0])