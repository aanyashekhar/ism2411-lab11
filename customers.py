#reflection question 1: I would use bracket notation when a key is required.
#reflection question 2:this parrent reminds me of a pivot table. the python version can process more information more quicker. 


print ("exercise 1")
customer = {
    "name":"Alice Smith",
    "email":"alice.smith@example.com",
    "tier":"gold",
    "ytd_spend": 1200.00
}
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print("Full Dictionary:", customer)
print()

print ("exercise 2")
customer["phone"] = "555-1234"
print(customer["phone"])
customer["tier"] = "platinum"
print(customer["tier"])
del customer["email"]
print("After Deletion:", customer)
print()

print ("exercise 3")
email_lookup=customer.get("email", "Email not found")
print("safe lookup:", email_lookup)
try:
    email_bracket=customer["email"]
    print("bracket lookup:", email_bracket)
except KeyError:
    print("bracket lookup: Email not found")
print()

print("exercise 4")
for key, value in customer.items():
    print(key, ":", value)
print()

print("exercise 5")
tier_discounts = {
    "bronze": 0.05,
    "silver": 0.10,
    "gold": 0.15,
    "platinum": 0.20
}

purchase_amount = 100.00
customer_tier = customer.get("tier", "bronze")
discount = tier_discounts.get(customer_tier, 0)
final_price = purchase_amount * (1 - discount)
print(f"Customer Tier: {customer_tier}")
print(f"Discount: {discount*100:.0f}%")
print(f"Final Price: ${final_price:.2f}")
print()

print("exercise 6")
customers = [
    { "name": "Alice Smith",
        "email": "alice.smith@example.com",
        "tier": "gold",
        "ytd_spend": 1200.00
    },
    { "name": "Bob Johnson",
        "email": "bob.johnson@example.com",
        "tier": "silver",
        "ytd_spend": 800.00
    },
    { "name": "Charlie Brown",
        "email": "charlie.brown@example.com",
        "tier": "bronze",
        "ytd_spend": 400.00
}
]

test_purchase = 300.00

for customer in customers:
    customer_name = customer.get("name", "Unknown")
    customer_tier = customer.get("tier", "bronze")
    rate = tier_discounts.get(customer_tier, 0)
    discounted_amount = test_purchase * (1 - rate)
    print(f"Customer: {customer_name}")
    print(f"Tier: {customer_tier}")
    print(f"Discounted Amount: ${discounted_amount:.2f}")
print()

print("exercise 7")
catalog = {
    "widget a":{"price": 10.00, "stock": 100},
    "gadget c":{"price": 20.00, "stock": 50},
    }

for item_name, details in catalog.items():
    if details.get("stock", 0) < 20:
        print(f"Low stock alert: {item_name} is in stock.")
print()

print("exercise 8")
transaction = [
    {"region": "North", "amount": 100.00},
    {"region": "South", "amount": 150.00},
    {"region": "East", "amount": 200.00},
    {"region": "West", "amount": 250.00}
]
sales_summary = {}
for tx in transaction:
    region = tx.get("region", "Unknown")
    amount = tx.get("amount", 0)
    sales_summary[region] = sales_summary.get(region, 0) + amount

for reg in sorted(sales_summary.keys()):
    print(f"Region: {reg}, Total Sales: ${sales_summary[reg]:.2f}")


