
def pairSumSequence(n):
    sum = 0
    for i in range(n):
        sum += pairSum(i, i+1)
    print(f"sequence sum: {sum}")
    return sum

def pairSum(a, b):
    print(f'added: {a} {b}')
    return a+b

pairSumSequence(10)