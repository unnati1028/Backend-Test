def oneToMultiDimensional(oneDimensional):
    multiDimensional = {}
    for key, value in oneDimensional.items():
        oneDimensional = multiDimensional
        keys = key.split('/')
        for idx, key in enumerate(keys[:-1]):
            if key not in oneDimensional:
                if keys[idx+1].isnumeric():
                    oneDimensional[key]=[]
                else:
                    oneDimensional[key]={}  
            prev=oneDimensional
            oneDimensional=oneDimensional[key]

        if keys[-1].isalpha():
            oneDimensional[keys[-1]]=value
        else:
            prev[key].append(value)
    return multiDimensional

testDict = {
                'one/two':3,
                'one/four/0':5,
                'one/four/1':6,
                'one/four/2':7,
                'eight/nine/ten':11
            }
print('\n---------- One dimensional to Multi-dimensional Transformation ----------')
print(oneToMultiDimensional(testDict))