
# Exercise 1

customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00
}

# Print each field individually
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])

# Print the entire dictionary
print(customer)



# Exercise 2

# Add a phone number
customer["phone"] = "555-123-4567"
print(customer)

# Update the tier
customer["tier"] = "platinum"
print(customer)

# Delete the email field
del customer["email"]
print(customer)



# Exercise 3

# Use .get() to look up the deleted email
email = customer.get("email", "no email on file")
print(email)

# Use bracket notation to look up the deleted email
try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")



# Exercise 4

# Print every key and value using .items()
for key, value in customer.items():
    print(f"{key}: {value}")

# Iterate without .items()
# Without .items(), the loop only gives us the keys,
# not both the keys and their values.
for key in customer:
    print(key)



# Exercise 5

# Create a dictionary of tier discounts
tier_discounts = {
    "bronze": 0,
    "silver": .05,
    "gold": .10,
    "platinum": .15
}

# Look up the customer's discount
discount_rate = tier_discounts.get(customer["tier"], 0)

# Calculate the discounted price
purchase_price = 200
final_price = purchase_price - (purchase_price * discount_rate)

# Print the results
print("Tier:", customer["tier"])
print("Discount rate:", discount_rate * 100, "%")
print("Final price: $", round(final_price, 2))



# Exercise 6

# Create three customer dictionaries
customers = [
    {"name": "Alice", "tier": "platinum"},
    {"name": "Bob", "tier": "gold"},
    {"name": "Charlie", "tier": "silver"}
]

# Loop through each customer
for customer_info in customers:
    tier = customer_info["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(f"{customer_info['name']} - {tier} - Discount: ${discount_amount:.2f}")
