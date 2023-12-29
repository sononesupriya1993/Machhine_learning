# Take p,n,r as input from user
p = float(input('Please enter principal value : '))
n = float(input('please enter no of years : '))
r = float(input('Please enter rate of interest : '))

# Calculate simple interest
i = p*n*r/100

#Calculate total amount
a = p+i

#print above results
print(f'Simple Interest : {i:2f} INR')
print(f'Total Amount : {a:2f} INR')
