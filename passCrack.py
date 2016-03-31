import sys
import hashlib
import mincemeat
domain="abcdefghijklmnopqrstuvwxyz0123456789"
all_possibilities=[]
datasource={}
hex_ip = sys.argv[1]
print 'Attacking '+str(hex_ip)

def gen(length, possibles):
  ret = []
  if length == 1:
    return list(possibles)
  else:
    s = gen(length -1, possibles)
    for c in possibles:
      for i in s:
        ret.append(str(c) + str(i))
  return ret

for x in range(1, 5):
    all_possibilities +=gen(x,domain)

temp = ''
counter = 0
for word in all_possibilities:
  temp = temp + word.rstrip() + ' '
  if counter % 10000 == 0:
    temp = temp + hex_ip
    datasource[counter] = temp
    temp = ''
  counter += 1
  
datasource[counter] = temp

def mapfn(k,v):
 import md5
 w_list=v.split()
 hash_w=w_list[-1]
 for w in w_list:
   w=w.strip()
   h=md5.new(w).hexdigest()
   if h[:5]==hash_w:
     yield w,hash_w

def reducefn(k,vs):
  return vs

s=mincemeat.Server()
s.datasource = datasource
s.mapfn = mapfn
s.reducefn =reducefn

results = s.run_server(password="changeme")
print results.keys()
