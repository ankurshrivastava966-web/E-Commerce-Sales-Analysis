import pandas as pd

# Load dataset
df = pd.read_csv("Dataset/raw_data.csv")

print("Original Shape:", df.shape)

# Remove duplicate records
df = df.drop_duplicates()

# Handle missing values
df["Customer_Name"] = df["Customer_Name"].fillna("Unknown")
df["Payment_Mode"] = df["Payment_Mode"].fillna("Unknown")

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# Create calculated columns
df["Sales"] = (
    df["Quantity"] * df["Unit_Price"] * (1 - df["Discount"])
)

df["Total_Cost"] = df["Quantity"] * df["Unit_Cost"]

df["Profit"] = df["Sales"] - df["Total_Cost"]

# Extract month and year
df["Month"] = df["Order_Date"].dt.month_name()
df["Year"] = df["Order_Date"].dt.year

# Save cleaned dataset
df.to_csv("Dataset/cleaned_data.csv", index=False)

print("Cleaning completed!")
print("Cleaned Shape:", df.shape)
print(df.head())