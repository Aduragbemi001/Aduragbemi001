#This code is used to get qualified age for driving
name=input("What is your name? ")
age=input("How old are you? ")
if int(age) >=18:
	print("Congratulations",name, "you're qualified to drive.")
elif int(age)>=16:
	print("Sorry!",name,"you're not qualified yet,but you still have to wait for 1 - 2 years.")
else:
	print("Sorry!",name,"you're not qualified to drive.")