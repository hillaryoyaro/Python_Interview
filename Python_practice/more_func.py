def hellofunc(greatings,name = 'Hillary'):
    return '{} {}'.format(greatings,name)

print(hellofunc("What is you","Norman"))


def student_information(*args,**kwargs):
    print(args)
    print(kwargs)
    #return"{}{}".format(args,kwargs)
course = ['Math','Art']
infor = {'name':'Hillary','age':28}
student_information('Math','Art' ,name = 'John',age = 27) 
# to unpack the list and dictionary we use the single star and double star
# to the function call
student_information(*course,**infor)   