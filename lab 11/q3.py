import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

np.random.seed(42)
n = 30

df = pd.DataFrame({
    'id':[f'S{i:03d}' for i in range(1,n+1)],
    'gpa':np.random.uniform(1.5,4.0,n).round(2),
    'hrs':np.random.uniform(2,25,n).round(1),
    'att':np.random.uniform(40,100,n).round(1)
})

X = df[['gpa','hrs','att']]

sc = StandardScaler()
Xs = sc.fit_transform(X)

wcss = []
for k in range(2,7):
    wcss.append(KMeans(n_clusters=k, random_state=42).fit(Xs).inertia_)

plt.plot(range(2,7), wcss)
plt.show()

k = 3
km = KMeans(n_clusters=k, random_state=42)
df['c'] = km.fit_predict(Xs)

for i in range(k):
    m = df['c']==i
    plt.scatter(df[m]['hrs'], df[m]['gpa'], label=f'c{i}')

plt.legend()
plt.show()

print(df[['id','gpa','hrs','att','c']])
print(df.groupby('c')[['gpa','hrs','att']].mean().round(2))