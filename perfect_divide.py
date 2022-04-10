
def pefect_num():
    """
     generator that find a perfect number-
     A perfect number is a number whose division (without 1) is equal to itself
    """
    counter = 2 #1 divides each number so we'll start with 2
    while counter:
        temp_sum = 0
        list_of_divide = [temp for temp in range(1, counter) if(counter % temp == 0)]
        temp_sum = sum(list_of_divide)
        if temp_sum == counter:
            yield temp_sum
        counter = counter+1

if __name__=="__main__":
    num_perfect=pefect_num()
    while 1:
        print(next(num_perfect))