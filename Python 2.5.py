subtotal=eval(input("Enter the subtotal:"))
gratuityrate=eval(input("Enter the gratuityrate:"))
gratuity=(subtotal/100*gratuityrate)
total=(gratuity+subtotal)
print("the gratuity is",gratuity,"and the total is",total)
