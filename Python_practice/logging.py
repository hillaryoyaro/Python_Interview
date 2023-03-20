import logging


logging.basicConfig(filename='test.log' level=logging>Deburg)
def add(x,y):
    """Addition of two parameter"""
    return x + y

def subtraction(x,y):
    """subtract x from y"""
    return x - y

def multiplication(x,y):
    """multiplication"""
    return x * y

def division(x,y):
    """division"""
    return x / y 

num_1 = int(input("Enter value of x"))
num_2 = int(input("Enter value of y"))

result_add = add(num_1,num_2)
logging.deburg("Add:{} + {} = {}".format(num_1,num_2,result_add))
result_sub = subtraction(num_1,num_2)
logging.debug("Sub:{} - {} = {}".format(num_1,num_2,result_sub))
result_mult = multiplication(num_1,num_2)
logging.debug("Mult:{} * {} = {}".format(num_1,num_2,result_mult))
result_div = division(num_1,num_2)
logging.debug("Div:{} / {} = {}".format(num_1,num_2,result_div))
