__author__ = 'agorgoma'


def Coma(list):
    string = ''
    for i in range(len(list)):
        if i < len(list)-1:
            string += (str(list[i]) + ',' + ' ')
        else:
            string += (str(list[i]) + '.')
    return string




spam = ['apples', 'bananas', 'tofu', 'cats']
eggs = [1,2,-3,'cat',5,6,7]

print(Coma(eggs))