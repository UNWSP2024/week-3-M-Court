# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 


#user chooses hot dog or chili dog
order = input("Would you like a hot dog or chili dog? ")

#assign order to a price
if order == "hot dog":
		order = 3.5
if order == "chili dog":	
		order = 4.5

#ask user if they want cheese
cheese = input("Would you like cheese? ")

#ask user if they want peppers
peppers = input("Would you like peppers? ")

#add condiment prices to order
if cheese == "yes" and peppers == "yes":
		subtotal = order + 1.5
if cheese == "yes" and peppers == "no": 
		subtotal = order + 0.5
if cheese == "no" and peppers == "yes":
		subtotal = order + 1
if cheese == "no" and peppers == "no":
    subtotal = order

#print subtotal 
print(f'Your subtotal is ${subtotal:.2f}')

#print tax
tax = subtotal * 0.07
print(f'Your tax is ${tax:.2f}')

total = subtotal + tax
#print total
print(f'Your total is ${total:.2f}.')