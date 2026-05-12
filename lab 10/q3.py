import pandas as pd
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

d = {
    'spend':[5000,200,8000,150,6500,300,9000,250,7000,180],
    'age':[35,22,45,19,38,25,50,21,42,20],
    'vis':[20,3,30,2,25,5,35,4,28,3],
    'freq':[10,1,15,1,12,2,18,2,14,1],
    'hv':[1,0,1,0,1,0,1,0,1,0]
}

df = pd.DataFrame(d)

X = df[['spend','age','vis','freq']]
y = df['hv']

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

sc = StandardScaler()
Xtr = sc.fit_transform(Xtr)
Xte = sc.transform(Xte)

svm = SVC(kernel='linear', C=1)
svm.fit(Xtr, ytr)

print("svm acc:", accuracy_score(yte, svm.predict(Xte))*100)
print("sv:", svm.n_support_)

dt = DecisionTreeClassifier(max_depth=3, random_state=42)
dt.fit(Xtr, ytr)

yp = dt.predict(Xte)

print("dt train:", dt.score(Xtr, ytr)*100)
print("dt test:", accuracy_score(yte, yp)*100)

for f,i in zip(['spend','age','vis','freq'], dt.feature_importances_):
    print(f, ":", i)

plt.figure(figsize=(8,5))
plot_tree(dt, feature_names=['spend','age','vis','freq'], class_names=['0','1'], filled=True)
plt.show()