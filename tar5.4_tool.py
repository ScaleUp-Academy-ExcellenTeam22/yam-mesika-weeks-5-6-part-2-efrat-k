
def find_min(*interleave):
    """
       function that return the min length of the argument
    """
    min_lenght = interleave[0]
    min_len = len(interleave[0])
    for item in interleave:
        if min_len > len(item):
            min_lenght = item
    return min_lenght

"""
    A function that receives several lists and returns one list in the requested order
    For example for [1,2,3] [#,*,+] return- [1,#,2,*,3,+]
"""
def interleave(*interleave): #interleave- A variable that can have several lists
    count_iteration = 0
    rest_interleave = []
    for i in interleave:
        rest_interleave += [i]
    while rest_interleave:
        current_item = find_min(*rest_interleave)
        for i in range(len(current_item)-count_iteration):
            listt = []
            for item in rest_interleave:
                listt += [item[count_iteration]]
            yield listt
            count_iteration += 1
        temp = rest_interleave
        rest_interleave = []
        for it in temp:
            if not len(it) == len(current_item):
                rest_interleave += [it]


if __name__=="__main__":

    func1 = interleave('abc', [1, 2], ('!', '@', '#'))
    all=[]
    for i in func1:
        all+=i
    print(all)

