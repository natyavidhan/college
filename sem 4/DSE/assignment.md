# ✅ **1. NumPy Programs**

```python
import numpy as np

# a
ARR1 = np.random.rand(3, 4)
print("Array:\n", ARR1)
print("Mean:", np.mean(ARR1, axis=1))
print("Std:", np.std(ARR1, axis=1))
print("Variance:", np.var(ARR1, axis=1))

# b
m = int(input("Enter m: "))
n = int(input("Enter n: "))
arr = np.random.randint(1, 100, (m, n))
print(arr)
print("Shape:", arr.shape)
print("Type:", type(arr))
print("Dtype:", arr.dtype)
reshaped = arr.reshape(n, m)
print("Reshaped:\n", reshaped)

# c
arr1d = np.array([0, 1, np.nan, 5, 0])
print("Zero indices:", np.where(arr1d == 0))
print("Non-zero indices:", np.where(arr1d != 0))
print("NaN indices:", np.where(np.isnan(arr1d)))

# d
A1 = np.random.rand(5)
A2 = np.random.rand(5)
A3 = np.random.rand(5)
A4 = A3 - A2
A5 = 2 * A1
print("Covariance:", np.cov(A1, A4))
print("Correlation:", np.corrcoef(A1, A5))

# e
A1 = np.random.randint(1, 10, 10)
A2 = np.random.randint(1, 10, 10)
print("Sum first half:", np.sum(A1[:5] + A2[:5]))
print("Product second half:", np.prod(A1[5:] * A2[5:]))

# f
arr = np.random.rand(10, 10)
print("Memory size:", arr.nbytes, "bytes")

# g
m, n = 3, 4
arr = np.random.randint(10, 100, (m, n))
print(arr)
arr[[0,1]] = arr[[1,0]]  # swap rows
arr2 = arr.copy()
arr2[:,1] = arr2[::-1,1]  # reverse column
print(arr2)
```

---

# ✅ **2. Pandas Series**

```python
import pandas as pd
import numpy as np

# a
s = pd.Series([5, 2, 9, 1, 7])
print(s.sort_index())
print(s.sort_values())

# b
s = pd.Series([10, 20, 20, 30, 10])
print("Rank first:\n", s.rank(method='first'))
print("Rank max:\n", s.rank(method='max'))

# c
print("Min index:", s.idxmin())
print("Max index:", s.idxmax())
```

---

# ✅ **3. DataFrame Operations**

```python
df = pd.DataFrame(np.random.randn(50, 3), columns=['A','B','C'])

# introduce nulls
for _ in range(int(0.1 * df.size)):
    i = np.random.randint(0,50)
    j = np.random.randint(0,3)
    df.iat[i,j] = np.nan

# a
print(df.isnull().sum())

# b
df = df.dropna(axis=1, thresh=45)

# c
df = df.drop(df.sum(axis=1).idxmax())

# d
df = df.sort_values(by='A')

# e
df = df.drop_duplicates(subset='A')

# f
print("Correlation:", df['A'].corr(df['B']))
print("Covariance:", df['B'].cov(df['C']))

# g
df['B_bins'] = pd.cut(df['B'], bins=5)
print(df)
```

---

# ✅ **4. Excel Merge**

```python
df1 = pd.read_excel("file1.xlsx")
df2 = pd.read_excel("file2.xlsx")

# a
print(pd.merge(df1, df2, on="Name"))

# b
print(pd.concat([df1, df2]).drop_duplicates(keep=False))

# c
merged = pd.concat([df1, df2])
print(len(merged))

# d
merged.set_index(['Name','Date'], inplace=True)
print(merged.describe())
```

---

# ✅ **5. Iris Dataset**

```python
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

iris = load_iris(as_frame=True)
df = iris.frame

# a
print(df.info())

# b
print(df.isnull().sum())

# c
df['target'].value_counts().plot(kind='bar')
plt.show()

# d
sns.regplot(x='sepal length (cm)', y='petal length (cm)', data=df)
plt.show()

# e
df['petal width (cm)'].plot(kind='density')
plt.show()

# f
sns.pairplot(df, hue='target')
plt.show()

# g
sns.heatmap(df[['sepal length (cm)','petal length (cm)']].corr(), annot=True)
plt.show()

# h
print(df.describe())

# i
sns.heatmap(df.corr(), annot=True)
plt.show()
```

---

# ✅ **6. Titanic Dataset**

```python
titanic = sns.load_dataset('titanic')

# a
titanic = titanic.dropna(axis=1, thresh=500)

# b
print(len(titanic[titanic['age'] > 30]))

# c
print(titanic[titanic['class']=='Second']['fare'].sum())

# d
print(titanic.groupby('class')['survived'].sum())

# e
print(titanic.groupby('sex')['age'].describe())

# f
sns.scatterplot(x='fare', y='age', hue='sex', data=titanic)
plt.show()

# g
sns.kdeplot(titanic['age'])
sns.kdeplot(titanic['fare'])
plt.show()

# h
titanic['class'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.show()

# i
print(titanic.groupby('class')['survived'].mean()*100)
```

👉 Conclusion: Yes, higher class → higher survival rate.

---

# ✅ **7. Family Income**

```python
data = {
'Family':['Shah','Vats','Vats','Kumar','Vats','Kumar','Shah','Shah','Kumar','Vats'],
'Gender':['Male','Male','Female','Female','Female','Male','Male','Female','Female','Male'],
'Income':[44000,65000,43150,66500,255000,103000,55000,112400,81030,71900]
}

df = pd.DataFrame(data)

# a
print(df.groupby('Family')['Income'].sum())

# b
print(df.groupby('Family')['Income'].agg(['max','min']))

# c
print(df[df['Income'] < 80000])

# d
females = df[df['Gender']=='Female']
print(len(females), females['Income'].mean())

# e
avg = df['Income'].mean()
df = df[df['Income'] >= avg]
print(df)
```