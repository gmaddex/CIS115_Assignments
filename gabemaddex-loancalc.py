#Gabe Maddex
#Scholars Section
#This program calculates a loan based on data provided by the userd
print "Welcome to the loan calculator program"
principal = input("Enter your principal value: ")
rate = input("Enter your interest rate as a decimal: ")
years = input("Enter the amount of years: ")

annualPayment = (((1 + rate) ** years) * principal * rate) / (((1 + rate) ** years) -1)
print "\n Your annual payment is: $" + str("{:,.2f}".format(annualPayment)) + "\n"

monthlyPayment = annualPayment / 12
print "\n Your monthly payment is: $" + str("{:,.2f}".format(monthlyPayment)) + "\n"

print "\n The total amount paid for the life of the loan is: $" + str("{:,.2f}".format(annualPayment * years)) + "\n"
