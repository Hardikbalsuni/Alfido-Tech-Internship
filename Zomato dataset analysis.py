
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the dataset
df = pd.read_csv("zomato.csv", encoding="latin1")

# Data Cleaning
df['rate'] = df['rate'].astype(str).apply(lambda x: x.strip().replace('/5', '') if '/' in x else x)
df['rate'] = df['rate'].replace(['NEW', '-', 'nan'], pd.NA)
df['rate'] = pd.to_numeric(df['rate'], errors='coerce')

df['approx_cost(for two people)'] = (
    df['approx_cost(for two people)'].astype(str).str.replace(',', '').replace('nan', pd.NA)
)
df['approx_cost(for two people)'] = pd.to_numeric(df['approx_cost(for two people)'], errors='coerce')
df['votes'] = pd.to_numeric(df['votes'], errors='coerce')

df = df.dropna(subset=[
    'rate', 'votes', 'approx_cost(for two people)', 'online_order', 'book_table', 'location', 'cuisines'
])

# Create folder for charts
os.makedirs("charts", exist_ok=True)

# Plot: Bar chart for online_order
sns.set(style="whitegrid")
plt.figure(figsize=(6, 5))
sns.countplot(x='online_order', data=df, palette='pastel')
plt.title("Online Order Availability")
plt.xlabel("Online Order (Yes/No)")
plt.ylabel("Number of Restaurants")
plt.tight_layout()
plt.savefig("charts/online_order_bar.png")
plt.show()
