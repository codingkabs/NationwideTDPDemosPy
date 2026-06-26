def changecase(function):
    return function().upper()


@changecase
def myFunctionName(name):
    return "Hello " + name

print(myFunctionName("Jordan"))

# @changecase
# def myfunction():
#   return "Hello Sally"
#
# @changecase
# def myfunction1():
#   return "Hello Jordan"
#
# @changecase
# def myfunction2():
#   return "Hello Melanie"
#
# print(myfunction)
# print(myfunction1)
# print(myfunction2)