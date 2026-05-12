import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler

d = {
    'free':[0.8,0.0,0.9,0.0,0.7,0.0,0.6,0.1,0.85,0.0],
    'money':[0.7,0.0,0.8,0.0,0.6,0.0,0.5,0.0,0.75,0.0],
    'len':[500,200,450,180,520,150,480,220,510,170],
    'links':[5,1,6,0,4,1,5,2,7,0],
    'known':[0,1,0,1,0,1,0,1,0,1],
    'spam':[1,0,1,0,1,0,1,0,1,0]
}

df = pd.DataFrame(d)

X = df.drop('spam', axis=1)
y = df['spam']

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.3, random_state=42)

sc = StandardScaler()
Xtr = sc.fit_transform(Xtr)
Xte = sc.transform(Xte)

svm = SVC(kernel='rbf', C=1, gamma='scale')
svm.fit(Xtr, ytr)

yp = svm.predict(Xte)

print("acc:", accuracy_score(yte, yp)*100)
print(classification_report(yte, yp))
print(confusion_matrix(yte, yp))

new = pd.DataFrame({
    'free':[0.75],
    'money':[0.65],
    'len':[480],
    'links':[6],
    'known':[0]
})

new = sc.transform(new)

print("pred:", "SPAM" if svm.predict(new)[0]==1 else "NOT SPAM")