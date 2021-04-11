"""
    Linear Regression

    Dataset:
    X = [1,2,3,4,5]
    Y = [1,4,9,16,25]

    Linear regression line equation
    Y = b0 + b1X

"""
import numpy as np

class LinearRegressionModel:
    def __init__(self):
        self.b0 = 0
        self.b1 = 0
        self.mse = 0
        self.can_predict = False

    def fit(self, X, Y):
        self.X = X
        self.Y = Y

        self.b1 = np.sum((self.X - np.mean(self.X)) * (self.X - np.mean(self.Y))) / np.sum(np.square(self.X - np.mean(self.X)))
        print("b1 is: ", self.b1)

        self.b0 = np.mean(self.Y) - (self.b1 * np.mean(self.X))
        print("b0 is: ", self.b0)

        print("Equation of line: Y = {} + {} X".format(self.b0, self.b1))

        self.mse = np.sum(np.square(self.predict_Y_dash(self.X) - np.mean(self.Y))) / np.sum(np.square(self.Y - np.mean(self.Y)))
        print("MSE is: ",self.mse)  # Range of MSe is -> [0,1]

        if self.mse > 0 and self.mse < 1:
            self.can_predict = True

        return (self.b0, self.b1, self.mse, self.can_predict)

    def predict_Y_dash(self, X):
        Y_dash = self.b0 + np.multiply(self.b1, X)
        return Y_dash

    def predict(self, X):
        if self.can_predict:
            Y = self.b0 + np.multiply(self.b1, X)
            return Y
        else:
            return -1


def main():

    #1. DATASET
    X = [1, 2, 3, 4, 5]     # Independent Input Variable
    Y = [1, 4, 9, 16, 25]   # Dependent Output Variable

    #2. Create the model
    model = LinearRegressionModel()

    #3. Train the model
    result = model.fit(X, Y)
    print(result)

    #4. Predict from model
    predicted_Y = model.predict(6)
    print("For value 6 predicted value is: ", predicted_Y)

if __name__ == '__main__':
    main()