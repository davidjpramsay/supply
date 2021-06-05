# Variable Declarations
f1 = open("baublesin.txt", "r")
f2 = open("baublesout.txt", "w")
lines = []
order = []

# Read File
lines = f1.readlines()
order = lines[0].split()

# Declare Order and Supply Variables
supplyA = int(order[0])
supplyB = int(order[1])
spare = int(order[2])
orderA = int(order[3])
orderB = int(order[4])

# Define Orders Order Deficiencies and Order Over Supplys etc
defA = min(supplyA - orderA,0)
defB = min(supplyB - orderB,0)
overA = max(supplyA - orderA,0)
overB = max(supplyB - orderB,0)
spareAfterDefFilled = spare + defA + defB
defOfOtherNonZeroOrder = 0

# Program
# If the order can't be filled or it is a zero order.
if defA + defB + spare < 0 or ((orderA == 0) and (orderB == 0)):
    minkill = 0
else:
	# If no order for product A
    if (orderA) == 0:
        weakestNonZeroOrder = supplyB - orderB
    # If no order for product B
    elif (orderB) == 0:
        weakestNonZeroOrder = supplyA - orderA
    # There is an order for each product
    else:
        weakestNonZeroOrder = min(supplyA - orderA, supplyB - orderB)
        defOfOtherNonZeroOrder = min(max(defA, defB),0)

    minkill = weakestNonZeroOrder + defOfOtherNonZeroOrder + spare + 1

# Write Solution and Close Files
f2.write(str(minkill))
f1.close()
f2.close()
