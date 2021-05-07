from itertools import chain, combinations
def checkValidity(a, b, c):
     
    # check condition
    if (a + b <= c) or (a + c <= b) or (b + c <= a) :
        return False
    else:
        return True

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    l =  chain.from_iterable(combinations(s, r) for r in range(len(s)+1))
    l = [i for i in l if len(i)>=3]
    print(l)
 
array = [1,3,5,6,8,6]
powerset(array)