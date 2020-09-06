import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv('heart.csv')
df.head()
bins = ['sex', 'fbs', 'exang']
cats = ['cp', 'restecg', 'slope', 'thal']
ords = ['ca']
nums = ['age', 'oldpeak', 'trestbps', 'chol', 'thalach']
target = ['target']
df.cp = df.cp.replace({0:'Asympt.', 1:'Atypical', 2:'Non', 3:'Typical'})
df.restecg = df.restecg.replace({0:'LV hyper', 1:'Normal', 2:'ST-T wave'})
df.slope = df.slope.replace({0:'down', 1:'up', 2:'flat'})
df.thal = df.thal.replace({0:'NA', 1:'Fixed', 2:'Normal', 3:'Revers.'})
X_train, X_test, y_train, y_test = train_test_split(df,
                                                    df.target,
                                                    test_size = 0.2,
                                                    random_state = 42,
                                                    stratify = df.target)


fig = plt.figure(figsize=(8, 6))
fig.subplots_adjust(hspace=0.4, wspace=0.4, bottom=0.01, top=0.95)

for i, var in enumerate(cats):
    i = i + 1
    ax = fig.add_subplot(2, 2, i)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    sns.countplot(data = X_train, x = var, hue = 'target', ax = ax)
plt.savefig('static\graphimage.jpeg',bbox_inches='tight')
plt.show()


df.restecg = df.restecg.replace({'Normal':0, 'LV hyper':1, 'ST-T wave':1})
df.thal = df.thal.replace({'NA':0, 'Normal':0, 'Fixed': 1, 'Revers.': 1})
X_train, X_test, y_train, y_test = train_test_split(df,
                                                    df.target,
                                                    test_size = 0.2,
                                                    random_state = 42,
                                                    stratify = df.target)
bins = ['sex', 'fbs', 'exang', 'thal', 'restecg']
cats = ['cp', 'slope']

fig = plt.figure(figsize=(8, 6))
fig.subplots_adjust(hspace=0.4, wspace=0.4, bottom=0.01, top=0.95)

for i, var in enumerate(bins):
    i = i + 1
    ax = fig.add_subplot(2, 3, i)
    sns.countplot(data = X_train, x = var, hue = 'target', ax = ax)
plt.savefig('static\graphimage2.jpeg',bbox_inches='tight')
plt.show()
