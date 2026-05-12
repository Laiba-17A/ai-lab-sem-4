import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

d = {
    'id':[5,3,8,2,4,7,6,10,1,9],
    'mil':[150000,120000,250000,80000,100000,220000,180000,300000,75000,280000],
    'eff':[15,18,10,22,20,12,16,8,24,9],
    'cost':[5000,4000,7000,2000,3000,6500,5500,8000,1500,7500],
    'type':['SUV','Sedan','Truck','Hatchback','Sedan','Truck','SUV','Truck','Hatchback','SUV']
}

df = pd.DataFrame(d)

X = df[['mil','eff','cost']].values

wcss = []
for k in range(1,8):
    wcss.append(KMeans(n_clusters=k, random_state=42).fit(X).inertia_)

plt.plot(range(1,8), wcss)
plt.show()

km1 = KMeans(n_clusters=3, random_state=42)
c1 = km1.fit_predict(X)

sc = StandardScaler()
Xs = sc.fit_transform(X)

km2 = KMeans(n_clusters=3, random_state=42)
c2 = km2.fit_predict(Xs)

print(pd.DataFrame({'type':df['type'],'no_scale':c1,'scaled':c2}))

plt.scatter(df['mil'], df['cost'], c=c1)
plt.title("no scale")
plt.show()

plt.scatter(df['mil'], df['cost'], c=c2)
plt.title("scaled")
plt.show()