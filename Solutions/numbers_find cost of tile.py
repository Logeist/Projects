def main():
    print("Floor plan cost calculator")
    cost = float(input("What is the cost per foot?: "))
    width = float(input("What is the width of the floor?: "))
    length = float(input("What is the length of the floor?: "))
    area = width * length
    totalCost = area * cost
    print("The total cost of tiling your floor is: $", totalCost)

if __name__ == "__main__":
    main()
