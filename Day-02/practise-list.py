'''List and tuple are same but tuple is immutable.
calling a valure return the link type of the object whivh is not modified
'''
L=[10,2.55,'data', True]
type(L)


#dictionary
emp = {"name": 'sam', "age": 30, "city": 'pune'}
print(emp)
print(len(emp))
#adding new element
emp["salary"] = 50000 # adding new elemen
print(emp)
emp['name'] = 'Jan' #modifing
print (emp)
#deleting an element
del emp['age']
print(emp)
#poping argument    
emp.pop('salary')
print(emp)