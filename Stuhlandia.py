

"""
:param recive path of file
:return the country that can be raiten in one line in the keyboard
"""
def find_special_state(path):
    line1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
    line2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
    line3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
    states = open(path, 'r')
    name_country= states.read()
    country=name_country.split('\n')
    list_country=[]
    for i in country:
        letter = [i[j] for j in range(len(i))]
        set_letter = set(letter)
        if  (line1.issuperset(set_letter)) or (line2.issuperset(set_letter)) or  (line3.issuperset(set_letter)):
            list_country.append(i)
    return list_country

if __name__=="__main__":
    print(find_special_state(r"C:\Users\efrat\OneDrive\Desktop\states.txt"))


