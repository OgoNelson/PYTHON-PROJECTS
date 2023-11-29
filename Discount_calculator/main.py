print("Thank you for shopping with us")
bill = float(input("Enter your bill\n"))

if bill >= 500:
    discountApplied = "15%"
    discount = bill * 0.15
    newBill = bill - discount
    print(f"Your initial bill is {bill}\n The discount given is {discountApplied}\n New bill is {round(newBill, 2)}")
else:
    discountApplied = "7%"
    discount = bill * 0.07
    newBill = bill - discount
    print(f"Your initial bill is ${bill}\n The discount given is {discountApplied}\n New bill is ${round(newBill, 2)}")
