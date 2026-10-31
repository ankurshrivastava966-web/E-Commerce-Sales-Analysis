import pandas as pd
import numpy as np
import random
import os

random.seed(42)
np.random.seed(42)

products = {
    "Laptop": ("Electronics", 55000, 42000),
    "Mobile": ("Electronics", 20000, 14000),
    "Headphones": ("Electronics", 2000, 1000),
    "Keyboard": ("Electronics", 1200, 600),
    "Chair": ("Furniture", 5000, 3000),
    "Table": ("Furniture", 8000, 5000),
    "Notebook": ("Stationery", 100, 40),
    "Pen": ("Stationery", 20, 8),
    "Bag": ("Accessories", 1500, 800),
    "Watch": ("Accessories", 3000, 1800)
}

customers = [
    "Rahul", "Amit", "Priya", "Anjali", "Rohit",
    "Neha", "Vikas", "Pooja", "Karan", "Sneha"
]

states = {
    "Madhya Pradesh": "Central",
    "Maharashtra": "West",
    "Delhi": "North",
    "Uttar Pradesh": "North",
    "Rajasthan": "North",
    "Gujarat": "West",
    "Karnataka": "South",
    "Tamil Nadu": "South",
    "West Bengal": "East",
    "Bihar": "East"
}

payment_modes = ["UPI", "Credit Card", "Debit Card", "Cash", "Net Banking"]

data = []

for i in range(1, 1001):
    product = random.choice(list(products.keys()))
    category, price, cost = products[product]

    quantity = random.randint(1, 5)
    discount = random.choice([0, 0.05, 0.10, 0.15])

    state = random.choice(list(states.keys()))

    data.append({
        "Order_ID": f"ORD{i:04d}",
        "Order_Date": pd.Timestamp("2025-01-01") +
                      pd.Timedelta(days=random.randint(0, 364)),
        "Customer_Name": random.choice(customers),
        "Product": product,
        "Category": category,
        "Quantity": quantity,
        "Unit_Price": price,
        "Unit_Cost": cost,
        "Discount": discount,
        "Region": states[state],
        "State": state,
        "Payment_Mode": random.choice(payment_modes)
    })

df = pd.DataFrame(data)

# Add a few missing values for cleaning practice
df.loc[5, "Payment_Mode"] = np.nan
df.loc[15, "Customer_Name"] = np.nan

# Add duplicate records for cleaning practice
df = pd.concat([df, df.iloc[:10]], ignore_index=True)

os.makedirs("Dataset", exist_ok=True)

df.to_csv("Dataset/raw_data.csv", index=False)

print("Dataset generated successfully!")
print("Total records:", len(df))
print(df.head())