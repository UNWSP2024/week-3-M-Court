# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 


#user chooses Hot Dog or Chili Dog
order = input("Would you like a hot dog or chili dog? ")

if order == "Hot Dog":
		order = float(3.5)
if order == "Chili Dog":	
		order = float(4.5)

#ask user if they want cheese
cheese = input("Would you like cheese? ")

#ask user if they want peppers
peppers = input("Would you like peppers? ")

if cheese == "yes" and peppers == "yes":
		subtotal = float(f"{order + 1.5}")
if cheese == "yes" and peppers == "no": 
		subtotal = float(f"{order + 0.5}")
if cheese == "no" and peppers == "yes":
		subtotal == float(f"{order + 1}")

#print subtotal 
print(f'Your subtotal is ${subtotal:.2f}')

#print tax
tax = subtotal * 0.07
print(f'Your tax is ${tax:.2f}')

total = subtotal + tax
#print total
print(f'Your total is ${total:.2f}.')
