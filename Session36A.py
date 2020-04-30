from sklearn import tree

# SUPERVISED MACHINE LEARNING :)
# CLASSIFICATION PROBLEM

# Representing Training Data

bike = 0
car = 1

bike1 = [200, 100]

X = [
        bike1, [250, 200], [300, 300], [350, 350],
        [800, 800], [1000, 1100], [1200, 1300], [1500, 1550]
    ]
Y = [bike, bike, bike, bike, car, car, car, car]

# Evaluation + Optimization

# Creating the Model
model = tree.DecisionTreeClassifier()

# Training the Model
model = model.fit(X, Y)

# Start Making Predictions :)
result = model.predict([[1220, 1120], [220, 110]])

print(result)