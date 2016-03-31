import mincemeat
import sys
import random

data = random.sample(xrange(2,(10**7)+1), 9999999)


temp = ''
counter = 0
datasource = {}
for i in data:
    i=str(i)
    temp = temp +  i.rstrip() + ' '  
    # print cousnter
    if counter % 500 == 0:    
        datasource[counter] = temp
        temp = ''
    counter += 1
if temp!= '':
    datasource[counter] = temp

def mapfn(k, v):
    def isPrime(n):
        if n==2 or n==3 or n==5 or n==7:
            return True
        if n<2 or n%2 ==0 or n%3==0 or n%5==0 or n%7==0:
            return False
        else:
            for x in range(11,int(n**0.5)+1,2):
                if n%x==0:
                    return False
            return True
    def isPalindrome(m):
        pal=str(m)[::-1]
        return str(m)==pal
    for i in v.split():
        i=int(i)
        if isPrime(i) and isPalindrome(i):

            yield 'Palindromic Prime', i
            yield 'Count', 1
            yield 'sum', i

def reducefn(k, vs):
    if k=='Palindromic Prime':
        result=[]
    
        for x in vs:
            result.append(x)
        return sorted(result)
    if k=='Count':
        return sum(vs)
    if k=='sum':
        return sum(vs)


s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

results = s.run_server(password="changeme")
print results



