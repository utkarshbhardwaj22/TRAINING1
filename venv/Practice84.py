"""
Introduction to Machine Learning
"""

"""
1. Supervised Learning
    
    Procedure:
    1. Create DataSet
    2. Create ML Model(generally available as APIs)
    3. Feed Features and labels as Data to ML models
    4. Train the model
    5. Check for accuracy
    6. Make Predictions
    
"""
# Decision tree classifier
from sklearn import tree



#1. Creating Dataset
data_set_features = [
    [200,100],
    [220,125],
    [250,150],
    [250,180],
    [280,220],
    [300,250],
    [1000,800],
    [1400,1250],
    [1500,1450],
    [1750,1500],
    [2000,1700],
    [2250,2000]
]

data_set_labels = [0,0,0,0,0,0,1,1,1,1,1,1]

lables = ["Bike", "Car"]

#2. Create ML Model
model = tree.DecisionTreeClassifier()

#3. Feed feartures and labels
#4. Train the model
model.fit(data_set_features, data_set_labels)

#5. Make predictions
known_observation = [220,125]
unknown_observation = [350,225]

result = model.predict([known_observation,unknown_observation])
print(lables[result[0]], lables[result[1]])


