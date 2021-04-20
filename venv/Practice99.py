"""
Support vector machines for classification

"""
from sklearn import svm


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
model = svm.SVC()

#3. Feed feartures and labels
#4. Train the model
model.fit(data_set_features, data_set_labels)

#5. Make predictions
known_observation = [220,125]
unknown_observation = [2250,2000]

result = model.predict([known_observation,unknown_observation])
print(lables[result[0]], lables[result[1]])