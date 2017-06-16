#words=input("Enter the number of words to find the length of max")
list1 = ['Avinash','SANKARASETTY','ASPK']
mx=0
worder=max(list1, key=len)
print(worder)
for word in list1:
    if len(word)>mx:
        mx=len(word)

print(mx)