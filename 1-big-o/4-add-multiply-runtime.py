import datetime

N = 1000

def addRunTimes(A, B):
    for a in A:
        print(a)

    for b in B:
        print(b)

A = list(range(1, N))
B = list(range(1,N))

timeStart = datetime.datetime.now()
addRunTimes(A,B)
T1 = datetime.datetime.now() - timeStart

def multiplyRunTimes(A,B):
    for a in A:
        for b in B:
            print(f"{a}, {b}")

timeStart = datetime.datetime.now()
multiplyRunTimes(A,B)
T2 = datetime.datetime.now() - timeStart

print(f"T1 = {T1}")
print(f"T2 = {T2}")