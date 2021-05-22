"""
    Introduction to Machine Learning
    Writing Perceptron
"""

class Perceptron:

    def __init__(self, inputs=None):
        self.inputs=inputs
        print("Preceptron Created.")
        print(inputs)

    def summation(self):
        self.sum = 0

        for i in range(len(self.inputs)):
            self.sum += self.inputs[i][0] * self.inputs[i][1]

        print("Summation function output: ", self.sum)

    def activation(self):

        theta = 0.5

        if self.sum>theta:
            print("Output is 1.")
        else:
            print("Output is 0.")


def main():
    input = [
        [0,0], #[input, weight]
        [0, 1],
        [1, 0],
        [1, 1]
    ]

    perceptron = Perceptron(inputs=input)
    perceptron.summation()
    perceptron.activation()



if __name__ == '__main__':
    main()