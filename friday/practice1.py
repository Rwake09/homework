# the print function is built into python
# it is a named block of code that does something useful
# we can call our function as many times aas we need


print('Hello World!!!!!')
print('Hello Rob!!!')

def solutions(s):
    countB = s.count('B')
    countA = s.count('A')
    countN = s.count('N')
    return min(countB, countA // 3, countN // 2)

s = 'BANBANBANBANBANBABNABANBNABNABNABNABNABNABN'
result = solutions(s)
print(result)

