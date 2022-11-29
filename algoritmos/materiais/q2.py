l = [2,3,4,5,6,7,8,9,10]

def a(l): return max(l)

def b(l): return sum(l)

def c(l): return l.count(l[0])

def d(l): return sum(l)/len(l)

def e(l):l2 = [d(l)]*len(l);l3=[abs(l2[i]-l[i]) for i in range(len(l))];l4 = l3[:];l4.sort();vmpz=l4[0];p=l3.index(vmpz);return l[p]

def f(l):vn = [i for i in l if i < 0];return sum(vn)

def g(l):
    cont = 0 
    for i,v in enumerate(l):
        if i==0:va=v;continue
        if v==va:cont+=1;va=v
        else:va=v
    return cont


print(a(l=l))
print(b(l=l))
print(c(l=l))
print(d(l=l))
print(e(l=l))
print(f(l=l))
print(g(l=l))