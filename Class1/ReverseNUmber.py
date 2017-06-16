#python code for the reverse a number

a=input('ENTER THE NUMBER TO BE REVERSED :')
number=int(a)
rev=0
#loop for the reverse a number
while(number>0):

   reminder=number%10
   number=number//10
   rev=rev*10+reminder

print('The Reverse of the number: ',rev)