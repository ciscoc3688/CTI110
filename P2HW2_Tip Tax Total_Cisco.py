# CTI-110 
# P2HW2 - Tip Tax Total
# 02/21/2018
#


print("")
mealprice = float(input("What was the price of your meal? $"))
print("")
tax = mealprice * .07
tip = .18 * mealprice
totalcost = mealprice + tax + tip
print ("Total: $"+format(totalcost,",.2f"))
print ("Tax: $"+format(tax,",.2f"))
print ("Tip: $"+format(tip,",.2f")) 
