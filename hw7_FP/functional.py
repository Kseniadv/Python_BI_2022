#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def sequential_map(*args):
    result=map(args[0], args[-1])
    for func in args[1:-1]:
        result=map(func,list(result))   
    return list(result)

def consensus_filter(*args):
    result=filter(args[0], args[-1])
    for func in args[1:-1]:
        result=filter(func,list(result))   
    return list(result)

def conditional_reduce(func1, func2, conteiner):
    new_conteiner = []
    try:
        for i in conteiner:
            if func1(i)==True: 
                new_conteiner.append(i)
        values_x = new_conteiner[0]
    except IndexError:
        return print("В контейнере не содержится значений, удовлетворяющих условию первой функции")
    for i in new_conteiner[1:]:
        values_x = func2(values_x, i)        
    return values_x


#Выводит ответ для каждой функции, последовательное выполнение функций не получилось
def func_chain(*args): 
    func = lambda x: [i(x) for i in args]
    return func

