#get item weight from user
weight_in_lbs = (float(input("Enter the package weight in pounds: ")))

#calculate shipping based on weight from user
#multiply weight by cost per lbs
if weight_in_lbs <= 2:
		shipping = weight_in_lbs * 1.5
if weight_in_lbs > 2 and weight_in_lbs <= 6: 
		shipping = weight_in_lbs * 3
if weight_in_lbs > 6 and weight_in_lbs <= 10: 
		shipping = weight_in_lbs * 4
if weight_in_lbs > 10: 
		shipping = weight_in_lbs * 4.75

#print total shipping charge
print(f'The total shipping charge is ${shipping:.2f}')