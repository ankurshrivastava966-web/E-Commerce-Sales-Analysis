import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("Dataset/cleaned_data.csv")

os.makedirs("Reports/Charts", exist_ok=True)

# 1. Overall KPIs
print("Total Sales:", round(df["Sales"].sum(), 2))
print("Total Profit:", round(df["Profit"].sum(), 2))
print("Total Orders:", df["Order_ID"].nunique())
print("Total Quantity:", df["Quantity"].sum())

# 2. Category-wise sales
category_sales = df.groupby("Category")["Sales"].sum()

print("\nCategory-wise Sales:")
print(category_sales)

category_sales.plot(kind="bar", title="Category-wise Sales")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("Reports/Charts/category_sales.png")
plt.close()

# 3. Region-wise profit
region_profit = df.groupby("Region")["Profit"].sum()

print("\nRegion-wise Profit:")
print(region_profit)

region_profit.plot(kind="bar", title="Region-wise Profit")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("Reports/Charts/region_profit.png")
plt.close()

# 4. Top 5 products
top_products = (
    df.groupby("Product")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print("\nTop 5 Products:")
print(top_products)

top_products.plot(kind="bar", title="Top 5 Products")
plt.tight_layout()
plt.savefig("Reports/Charts/top_products.png")
plt.close()

# 5. Monthly sales trend
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

monthly_sales = (
    df.groupby(df["Order_Date"].dt.to_period("M"))["Sales"]
    .sum()
)

monthly_sales.plot(kind="line", marker="o",
                   title="Monthly Sales Trend")

plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Reports/Charts/monthly_sales.png")
plt.close()

print("\nAnalysis completed successfully!")