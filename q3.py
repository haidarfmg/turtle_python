import math
loanAmount = eval(input("Enter Loan Amount : "))
numberOfYears = eval(input("Enter Number of Years : "))
annualInterestRate = eval(input("Enter Annual Interest Rate : "))


monthlyInterestRate = annualInterestRate / 1200

monthlyPayment = loanAmount * monthlyInterestRate/ (1 - 1 / pow(1 + monthlyInterestRate, numberOfYears * 12))

totalPayment = monthlyPayment * numberOfYears * 12

print("Monthly Payment: ",monthlyPayment)
print("Total Payment: ",totalPayment)

interest = loanAmount
principal = interest
balance = principal
print("interest  principal  balance")
for x in range(1, (numberOfYears * 12)+1):
   interest = monthlyInterestRate * balance;
   principal = monthlyPayment - interest;
   balance = balance - principal;
   
   print("{:.2f}".format(interest)," ","{:.2f}".format(principal)," ","{:.2f}".format(balance))
