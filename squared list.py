number=list(map(int,input('Enter a list :').split()))
def square(x):
    return x**2
square_list=map(square,number)
print('squared list is :',list(square_list))

# output
#
# Enter a list :4 5 2 9
# squered list is : [16, 25, 4, 81]