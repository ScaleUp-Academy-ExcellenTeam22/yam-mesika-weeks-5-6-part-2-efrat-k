import time

"""
A function that measures word search time in a particular data structure
"""
def average_runtime(words_list):
    start = time.time()
    time.sleep(1)
    for i in range(1000):
        if 'zwitterion' in words_list:
            pass
    end = time.time()
    return (end - start - 1)/100



if __name__=="__main__":
    f = open(r"C:\Users\efrat\Exellenteamm\PYTHON\tar5.2\word.txt", 'r')
    words_list = f.readline().split(" ")
    words_set = set(words_list)

    print("search in list: ",average_runtime(words_list))
    print("search in list: ",average_runtime(words_set))

