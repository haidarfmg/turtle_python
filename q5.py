name = str(input("Enter employee's name : "))
hours = eval(input("Enter number of hours worked in a week : "))
rate = eval(input("Enter hourly pay rate : "))
federalTax = eval(input("Enter federal tax withholding rate : "))
stateTax = eval(input("Enter state tax withholding rate : "))
grossPay = hours * rate
federalWithholding = grossPay * federalTax
stateWithholding = grossPay * stateTax
totalDeduction = federalWithholding + stateWithholding
netPay = grossPay - totalDeduction
print("\nEmployee Name: ", name)
print("\nHours Worked: ", hours)
print("\nPay Rate: ", rate)
print("\nGross Pay: ", rate)
print("Deductions:","\nFederal Withholding (20.0%) :",federalWithholding,
      "\nState Withholding (9.0%) :",stateWithholding,
      "\nTotal Deduction :",totalDeduction)
