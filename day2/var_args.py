def my_function(*args):
    print(args, type(args))
    print(args[0], args[-1])
my_function(10)
my_function(4,6,78,90)
my_function([1,3,5], 90, 78)
my_function()