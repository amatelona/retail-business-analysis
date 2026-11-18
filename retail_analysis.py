import pandas as pd

# Load dataset
df = pd.read_csv("Sample_Superstore.csv", encoding="latin1")

# Display first five rows
print(df.head())

# Check dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Display statistical summary
print(df.describe())
# Analyze sales and profit by category
category_analysis = df.groupby("Category").agg({
    "Sales": "sum",
    "Profit": "sum"
})

print("\nSales and Profit by Category:")
print(category_analysis)

# Analyze profit by sub-category
subcategory_analysis = df.groupby("Sub-Category")["Profit"].sum()

print("\nProfit by Sub-Category:")
print(subcategory_analysis.sort_values())
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Sales by Category
plt.figure(figsize=(7, 4))
sns.barplot(data=df, x="Category", y="Sales", estimator=sum)
plt.title("Sales by Category")
plt.savefig("sales_category.png")
plt.show()

# 2. Profit by Category
plt.figure(figsize=(7, 4))
sns.barplot(data=df, x="Category", y="Profit", estimator=sum)
plt.title("Profit by Category")
plt.savefig("profit_category.png")
plt.show()

# 3. Profit by Sub-Category
plt.figure(figsize=(10, 6))
sub = df.groupby("Sub-Category")["Profit"].sum().sort_values()
sns.barplot(x=sub.values, y=sub.index)
plt.title("Profit by Sub-Category")
plt.savefig("profit_subcategory.png")
plt.show()

# 4. Sales by Region
plt.figure(figsize=(7, 4))
region = df.groupby("Region")["Sales"].sum()
sns.barplot(x=region.index, y=region.values)
plt.title("Sales by Region")
plt.savefig("sales_region.png")
plt.show()
print("All charts created successfully!")