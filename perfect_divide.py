"""
 generator that find a perfect number
"""
def pefect_num():
    n=2
    while n:
        sum1 = 0
        l = [i for i in range(1, n) if(n % i == 0)]
        sum1 = sum(l)
        if sum1 == n:
            yield sum1
        n=n+1

if __name__=="__main__":
    num_perfect=pefect_num()
    while 1:
        print(next(num_perfect))