lst=[10,13,18,15,20]
def fun(x):
    if x%2!=0:
        return True
    else:
        return False
even_lst = list(filter(fun,lst))
print(even_lst)


even_lst = list(filter(lambda x : x%2!=0,lst))
print(even_lst)
