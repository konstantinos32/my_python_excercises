my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) 
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[2:4])
print(my_tuple[0:3])
print(my_tuple[1:])

if 3 in my_tuple:
    print("3 is in the tuple!")
    print(my_tuple.count(3))
    print(my_tuple.index(3))


    a, b, c, d, e = my_tuple
    print(a)

    x,*rest= my_tuple
    print(rest)

    another_tuple= (6, 7, 8)
    mulitipied_tuple = my_tuple(0)*2
    print(mulitipied_tuple)