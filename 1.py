'''
Input:
{
    'one':
    {
        'two': 3,
        'four': [ 5,6,7]
    },
    'eight':
    {
        'nine':
        {
            'ten':11
        }
    }
}
Output:
{
    'one/two':3,
    'one/four/0':5,
    'one/four/1':6,
    'one/four/2':7,
    'eight/nine/ten':11
}
'''


def keyGenerator(dataDict, data=None):
    updated_Keys = {}

    for keys in list(dataDict.keys()):
        if (type(dataDict[keys]) == list):
            for i in range(len(dataDict[keys])):
                updated_Keys['/'.join([str(data), str(keys), str(i)])
                             ] = dataDict[keys][i]
        elif (type(dataDict[keys]) == dict):
            updated_Keys.update(keyGenerator(
                dataDict[keys], '/'.join([str(data), str(keys)])))
        else:
            updated_Keys['/'.join([str(data), str(keys)])] = dataDict[keys]

    return updated_Keys


def multiToOneDimensional(multidimensional):
    oneDimensional = {}

    for keys in list(multidimensional.keys()):
        if (type(multidimensional[keys]) != dict):
            oneDimensional[keys] = multidimensional[keys]
        else:
            updated_Keys = keyGenerator(multidimensional[keys], keys)
            oneDimensional.update(updated_Keys)

    return oneDimensional


testDict = {'one': {
            'two': 3,
            'four': [5, 6, 7]},
            'eight': {
            'nine': {
            'ten': 11}}}

print('\n---------- Multi-dimensional to One dimensional Transformation ----------')
print(multiToOneDimensional(testDict))