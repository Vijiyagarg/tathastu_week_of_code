costPrice= float(input("Enter the cost price of product: "))
sellPrice= float(input("Enter the selling price of product: "))
profit= sellPrice - costPrice
newSellingPrice= 1.05 * profit + costPrice
print("The profit from this sell is", profit)
print("To increase the profit by 5% the selling price should be", newSellingPrice)
