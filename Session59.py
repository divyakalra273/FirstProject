import numpy as np
from sklearn.model_selection import KFold



X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]]) # Input Features
Y = np.array([1, 2, 3, 4])                     # Targets

kFold = KFold(n_splits=2)
print("Splits:", kFold.get_n_splits())

for train_index, test_index in kFold.split(X, Y):

    print("~~~~~~~~~~Indexes~~~~~~~~~~~~")
    print(train_index, test_index)
    print("~~~~~~~~~~~~~~~~~~~~~~")

    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]

    print("~~~~~~~~~~FOLD~~~~~~~~~~~~")
    print(X_train, X_test)
    print(Y_train, Y_test)
    print("~~~~~~~~~~~~~~~~~~~~~~")

    print()
