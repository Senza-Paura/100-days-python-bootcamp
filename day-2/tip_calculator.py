print ("Wlcome to your tip calcuator")

bill = float(input("what's the total bill? :  £ "))

tip = int(input("What percentage tip would you like to give ?, 10, 12, 15, ?"))

person = int(input("How many person are you ? "))



tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
total_bill = bill + total_tip_amount
bill_per_person =total_bill / person
final_amount = round(bill_per_person, 2)

print(f"each person should pay,  {final_amount} ")

