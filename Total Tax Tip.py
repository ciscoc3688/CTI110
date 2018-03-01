#Tax, Tip, and Total

print("")
mealprice = float(input("What was the price of your meal? $"))
print("")
tax = mealprice / 4.75
tip = .15 * mealprice
totalcost = mealprice + tax + tip
print ("Total: $"+format(totalcost,",.2f"))
print ("Tax: $"+format(tax,",.2f"))
print ("Tip: $"+format(tip,",.2f")) 
