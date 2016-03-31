
import mincemeat
import sys

inp_file = sys.argv[1]
file = open(inp_file,'r')
data = list(file)
file.close()
counter = 0
datasource = dict(enumerate(data))


def mapfn(k, v):
    yield 'count', 1
    yield 'sum', v
    yield 'stddev', int(v)
def reducefn(k, vs):
    import numpy
    result = 0
    counter = 0
    std_dev = 0
    if k == 'count':
        return sum(vs)
        
    if k == 'sum':
        return sum(vs)
            
    if k == 'stddev':
        std_dev = numpy.std(vs)
        return std_dev

s = mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn = reducefn

result = s.run_server(password="changeme")


print result
