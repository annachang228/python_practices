filled_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5,"F": 6,"G": 7,"H": 8,"I": 9,"J":10,"K": 11,"L": 12}
list1=["CDEF","ABC","FIJK"]
list1=sorted(list1)
newlist=[]
print list1
L1 =['ABC', 'CDEF', 'FIJK']
L2 = list("".join(L1))
print L2
for i in L2:
    x=filled_dict [i]
    newlist.append(x)
    print newlist
    z=reduce (lambda x , y : x + y , range (0,len(newlist)))
    print z



