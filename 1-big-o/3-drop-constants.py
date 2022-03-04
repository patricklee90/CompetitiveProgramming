import sys, datetime

#Min and Max 1

input = [1,3,4,56,7,3,12,6]

def minMax1(array):
    minVal = sys.maxsize
    maxVal = float('-inf')
    for id, x in enumerate(array):
        # print(f"round: {id}")
        if(x < minVal): minVal=x
        if(x > maxVal): maxVal=x

    print(f"min:{minVal}, max:{maxVal}")

timeStart = datetime.datetime.now()
print("method 1, array: [1,3,4,56,7,3,12,6]")
minMax1(input)
print(datetime.datetime.now() - timeStart)
#Min and Max 2

def minMax2(array):
    minVal = sys.maxsize
    maxVal = float('-inf')

    for id, x in enumerate(array):
        # print(f"round: {id}")
        if(x < minVal): minVal=x
    for id, x in enumerate(array):
        # print(f"round: {id}")
        if(x > maxVal): maxVal=x

    print(f"min:{minVal}, max:{maxVal}")

timeStart = datetime.datetime.now()
print("method 2, array: [1,3,4,56,7,3,12,6]")
minMax2(input)
print(datetime.datetime.now() - timeStart)