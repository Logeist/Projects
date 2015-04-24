import math


def quarters(total):
    quartersRaw = total / 0.25
    quarters = math.trunc(total / 0.25)
    change = (quartersRaw % 1) * 0.25
    dimes(change, quarters)


def dimes(change, quarters):
    dimesRaw = change / 0.10
    dimes = math.trunc(change / 0.10)
    change = (dimesRaw % 1) * 0.10
    nickels(change, quarters, dimes)


def nickels(change, quarters, dimes):
    nickelsRaw = change / 0.05
    nickels = math.trunc(change / 0.05)
    change = (nickelsRaw % 1) * 0.05
    pennies(change, quarters, dimes, nickels)


def pennies(change, quarters, dimes, nickels):
    pennies = math.trunc(change / 0.01)
    printResult(quarters,dimes,nickels,pennies)


def printResult(quarters, dimes, nickels, pennies):
	print("Quarters: ", quarters, "Dimes: " , dimes, "Nickels: ", nickels, "Pennies: ", pennies)


def main(quarters, nickels, pennies):
    cost = float(input("Enter the cost of the item: "))
    given = float(input("Money tendered: "))
    total = given - cost
    quarters(total)

if __name__ == "__main__":
    main(quarters, nickels, pennies)
