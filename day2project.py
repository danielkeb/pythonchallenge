print("welcome to the tip calculator")
total_bill = float(input("what was the total bill? $"))
tip_percentage = int(
    input("what percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("how many people to split the bill? "))
tip = total_bill * (12 / 100)
to_cap = total_bill + tip

pay = to_cap / people
pay = "{:.2f}".format(pay)
print(f"each person should pay: ${pay}")
