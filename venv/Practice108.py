"""
    KNN - K Nearest Neighbours

"""
import math

def e_distance(p1, p2):
    sum = 0
    for i in range(len(p1)):
        sum += math.pow((p1[i] - p2[i]),2)
    return math.sqrt(sum)


def main():

    data_set = [
        [65.34, 120.45],
        [68.23, 110.401],
        [70.96, 115.87],
        [60.24, 150.36],
        [71.45, 118.12],
        [66.83, 130.88],
        [69.91, 123.65],
        [75.02, 125.165],
        [73.21, 127.15],
        [78.76, 131.64]
    ]


    #Predict the weight of given height
    given_height = [66]

    k = 3  # In KNN K = 3 which means consider the closest 3 neighbours
    neighbour_distances = []
    for idx, data_point in enumerate(data_set):
        distance = e_distance(data_point[:-1], given_height)
        print("Distance between {} and {} is {}".format(data_point[:-1], given_height,distance))
        neighbour_distances.append((distance, idx))

    neighbour_distances = sorted(neighbour_distances)
    print(neighbour_distances)

    k_neighbour_distances = neighbour_distances[:k]
    print(k_neighbour_distances)

    # This is a Regression problem
    # we need to calculate the mean of output labels

    output_lables = []
    for neighbour in k_neighbour_distances:
        idx = neighbour[1]
        output_lables.append(data_set[idx][1])

    print(output_lables)

    predicted_weight = sum(output_lables) / len(output_lables)
    print("The predicted weight is {}".format(predicted_weight))

if __name__ == '__main__':
    main()