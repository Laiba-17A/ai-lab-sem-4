import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Mall_Customers.csv')

df = df.drop('CustomerID', axis=1)
df['Gender'] = df['Gender'].map({'Male':0,'Female':1})

X = df.values

wcss = []
for k in range(1,11):
    km = KMeans(n_clusters=k, random_state=42)
    km.fit(X)
    wcss.append(km.inertia_)

plt.plot(range(1,11), wcss)
plt.show()

km1 = KMeans(n_clusters=5, random_state=42)
c1 = km1.fit_predict(X)

plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=c1)
plt.title("no scale")
plt.show()

cols = ['Gender','Annual Income (k$)','Spending Score (1-100)']
sc = StandardScaler()

Xs = np.hstack([sc.fit_transform(df[cols]), df[['Age']].values])

km2 = KMeans(n_clusters=5, random_state=42)
c2 = km2.fit_predict(Xs)

plt.scatter(df['Annual Income (k$)'], df['Spending Score (1-100)'], c=c2)
plt.title("scaled")
plt.show()

print(pd.DataFrame({'no_scale':c1,'scaled':c2}).head(10))