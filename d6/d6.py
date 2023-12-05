#  TUPLE

tuple = ()
tuple1 = ("aaa","sss","ddd")
tuple = (111,222,333,4,5,6,7,8,9,0,1,1,1,1,1,1)
tuple3 = tuple+tuple1
print(tuple, tuple3)
print(len(tuple3))
tuple4 = tuple3[:3]
tuple5 = tuple3[-3:]
print(tuple4, tuple5)

del tuple4
print(111 in tuple3)