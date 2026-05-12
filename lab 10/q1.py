import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder

d = {
    'sqft':[1500,2000,1200,1800,2500,900,3000,1600,2200,1100],
    'bed':[3,4,2,3,5,2,5,3,4,2],
    'bath':[2,3,1,2,4,1,4,2,3,1],
    'age':[10,5,20,8,2,30,1,15,7,25],
    'nbr':['A','B','A','C','B','C','B','A','C','A'],
    'price':[250000,380000,180000,310000,520000,140000,650000,270000,420000,160000]
}

df = pd.DataFrame(d)



le = LabelEncoder()
df['nbr_enc'] = le.fit_transform(df['nbr'])

X = df[['sqft','bed','bath','age','nbr_enc']]
y = df['price']

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=42)

lr = LinearRegression()
lr.fit(Xtr, ytr)

print("b0:", lr.intercept_)
print("b:", lr.coef_)

yp = lr.predict(Xte)

print("r2:", r2_score(yte, yp))
print("rmse:", np.sqrt(mean_squared_error(yte, yp)))

new = pd.DataFrame({
    'sqft':[1700],
    'bed':[3],
    'bath':[2],
    'age':[12],
    'nbr_enc':[2]
})

print("pred:", lr.predict(new)[0])