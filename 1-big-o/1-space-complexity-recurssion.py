
def sum(n):
    
    if(n<=0):
        print(f'\t reach 0')
        return 0
    
    print(f'n: {n}')
    return n + sum(n-1)

sum(4)