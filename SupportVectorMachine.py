import sys
import math
import numpy as np
from scipy import optimize
from sklearn.datasets import load_iris

def MakeIrisDataset(irisDataset):
    data = irisDataset.data
    label = irisDataset.target
    dataFalse = data[label == 0]
    dataTrue = data[label == 1]

    numOfNineFalse = int(np.ceil(0.5 * len(dataFalse)))
    numOfNineTrue = int(np.ceil(0.5 * len(dataTrue)))

    dataForTraining = [dataFalse[:numOfNineFalse], dataTrue[:numOfNineFalse]]
    dataForTest = [dataFalse[numOfNineFalse:], dataTrue[numOfNineTrue:]]
    return dataForTraining, dataForTest

def CalculateMargin(weight, sv):
    margin = CalculateDistance(weight, sv[0]) + CalculateDistance(weight, sv[1])
    return margin

def CalculateDistance(weight, datum):
    # len(weight) + 1 == len(datum)
    distance = np.abs(DotProduct(weight[1:], datum) + weight[0]) / DotProduct(weight[1:], weight[1:])
    return distance

def MaximumMargin(data, initialWeight):
    dataClassTrue = data[0]
    dataClassFalse = data[1]
    
    weight = initialWeight
    while True:
        margins = [0, 1]
        marginCandidatesTrue = [CalculateDistance(weight, datum) for datum in dataClassTrue]
        marginCandidatesFalse = [CalculateDistance(weight, datum) for datum in dataClassFalse]

        # choose support vectors which are nearest data samples to the separation plane.
        [supportVectorTrue, indxTrue] = min(marginCandidatesTrue)
        [supportVectorFalse, indxFalse] = min(marginCandidatesFalse)

        sv = [dataClassTrue(indxTrue), dataClassFalse(indxFalse)]

        # maximize margin in respect of weight.
        [mgn, weight] = Maximize(weight, sv)

        margins[1] = margins[0]
        margins[0] = CalculateMargin(weight, sv)

        if margins[0] - margins[1] < 1:
            break

    return weight

def DotProduct(vector1, vector2):
    if len(vector1) != len(vector2):
        print('Error: Vector lengthes dont match.', file=sys.stderr)
        sys.exit(1)
    res = 0
    for scalar1, scalar2 in zip(vector1, vector2):
        res = res + scalar1 * scalar2
    return res

def SupportVectorMachine(data, weight, train=True):
    if train:
        resultWeight = MaximumMargin(data, weight)
        return resultWeight
    else:
        taggedData = []
        for datumVector in data:
            datumVector.append(1)
            selector = DotProduct(datumVector, weight)
            tag = selector > 0
            taggedData.append(tag)
        return taggedData

def main():
    iris_dataset = load_iris()
    [dataForTraining, dataForTest] = MakeIrisDataset(iris_dataset)
    dataSize = np.size(dataForTraining[0][0])
    weight = np.random.rand(dataSize + 1)

    weight = SupportVectorMachine(dataForTraining, weight, train=True)
    taggedData = SupportVectorMachine(dataForTest, weight, train=False)

if __name__ == '__main__':
    main()