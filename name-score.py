
# coding: utf-8

# In[69]:

filled_dict = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5,"F": 6,"G": 7,"H": 8,"I": 9,"J":10,"K": 11,"L": 12}
List1=["CDEF","ABC","FIJK"]
List1=sorted(list1)
newlist=[]
print List1
List1 =['ABC', 'CDEF', 'FIJK']
List2 = list("".join(List1))
print List2
for i in List2:
    x=filled_dict [i]
    newlist.append(x)
    print newlist
    z=sum(newlist)
    print z

