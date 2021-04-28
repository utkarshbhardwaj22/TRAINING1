"""
SelectKBest - Features Selection
Selects K best features

"""
from sklearn.datasets import load_iris
from sklearn.datasets import load_digits
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2

# X in uppercase is the Input
# y i lowercase is the acual output

X, y = load_digits(return_X_y=True)
print(X.shape)

X_new = SelectKBest(chi2, k=20).fit_transform(X, y)
print(X_new.shape) 