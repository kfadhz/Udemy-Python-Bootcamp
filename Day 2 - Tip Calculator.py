#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator")
bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
num_people = input("How many people to split the bill? ")

tip_percentage = float(tip) / 100
total_tip = tip_percentage * float(bill)
bill_tip = total_tip + float(bill)
split = bill_tip / int(num_people)

print(f"Each person should pay: ${round(split, 2)}")
