print("Welcome to the bill calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip do you want to give? 10, 12, or 15? "))
total_peep = int(input("How many people to split the bill? "))

divider = 1 + tip/100
result = (total_bill/total_peep)*divider
final_result = "{:.2f}".format(result)

print(f"Each person should pay: ${final_result}")
