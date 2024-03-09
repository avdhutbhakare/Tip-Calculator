print("Welcome to tip calculator! \n")

Bill= float(input("Enter the amount of Bill: "))
people=int(input("Total no of people: "))
Tip= int(input("Total percentage of tip you would like to offer? 10%, 12% or 15%: "))

Total_Tip= Bill/Tip
Total_Bill = Total_Tip + Bill
Bill_each = Total_Bill/people
Each=round(Bill_each, 2)
print(f"Each person has to pay ₹{Each}.")