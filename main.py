#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?


#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.


#asking for input
num = int(input("What number are you think of my friend? \n"))
#condition on checking if its an even or odd number 
if num%2==0:
    print("I like that you were thinking of an even number buddy!!")
else:
    print("Well that's an odd one !!")


  
if num%4 == 0:
    print("well it is also a multiple of 4")

num1 = int(input("Lets get another number from you --"))
num2 =int(input("Ok one last one buddy !!"))

if num1%num2 == 0 :
    print("Bingo")
else:
    print("No more games with you ! Loser!")
