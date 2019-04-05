import sys

def MaximumMargin(data):
    weight = []
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
        weight = MaximumMargin(data)
        return weight
    else:
        taggedData = []
        for datumVector in data:
            datumVector.append(1)
            selector = DotProduct(datumVector, weight)
            tag = selector > 0
            taggedData.append(tag)
        return taggedData

def main():
    dataForTraining = []
    dataForTest = []
    weight = []

    weight = SupportVectorMachine(dataForTraining, weight, train=True)
    taggedData = SupportVectorMachine(dataForTest, weight, train=False)

if __name__ == '__main__':
    main()