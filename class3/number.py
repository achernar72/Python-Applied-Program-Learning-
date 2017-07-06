
def my_function(a, b):
    b.append(a[0])
    b.append(a[-1])
    print(b)

a = ['1', '2', '3', '4', '5']
b=[]
my_function(a,b)
