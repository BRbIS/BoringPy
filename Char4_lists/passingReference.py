__author__ = 'agorgoma'


def eggs(someParameter):
    someParameter.append('Hello')

spam = [1, 2, 3]
p = spam
eggs(spam)
print(spam)
print(p)