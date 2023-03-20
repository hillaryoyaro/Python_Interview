from typing import Set,List,Dict,Callable,Sequence

#Create  a function that add two integers
def add(x:int,y:int) -> int:
    return x + y

#create a callable function
def foo(func:Callable[[int,int],int]) -> int:
     return (func(1,2))

x = foo(add)
print(x)    