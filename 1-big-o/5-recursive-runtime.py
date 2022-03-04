
def recursive(n):
    if(n<=1):
        return 1
    
    return recursive(n-1) + recursive(n-1)

    