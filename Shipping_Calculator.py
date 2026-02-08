#Shipping Calculator Cost

##Input package weight and shipping rate
weight = float(input("Enter the package weight in kilograms: "))
rate = float(input("Enter the shipping rate per kilogram: "))

#Calculate the shipping cost
shipping_cost = weight * rate

#Display the results
print(f"Shipping Cost: {shipping_cost} USD")
