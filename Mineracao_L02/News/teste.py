list = []
tuple = ("a","b","c")
list.append(tuple)
print(tuple)
for i in range(5):
    trio = (i,"string",i+2)
    print(trio)
    list.append(trio)
print(list)