immutable_var = (1, 'Привет', True)
print (immutable_var)
#immutable_var [0] = 5
print (immutable_var) # в кортедж входят неизменяемые объекты
mutable_list = [1, 'Привет', True]
mutable_list [0] = [5]
mutable_list [1] = True
mutable_list [2] = 'Пока'
print (mutable_list)