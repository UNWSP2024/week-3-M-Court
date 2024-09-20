#ask user for age 
age = int(input("Enter your age: "))

#display title based on age entered
if age <= 1:
    print("you are an infant")
if age > 1 and age < 13:
		print("you are a child")
if age >= 13 and age < 20:
		print("you are a teenager")
if age >= 20:
		print("you are an adult")