# Geospatial Data Analysis
# Business Expansion Analysis using Location-Based Data

import pandas as pd
import folium
import matplotlib.pyplot as plt

# ---------------------------------
# STEP 1: Load Dataset
# ---------------------------------

# Read CSV file
df = pd.read_csv("geospatial_data.csv")

print("First 5 Rows:\n")
print(df.head())

# ---------------------------------
# STEP 2: Data Cleaning
# ---------------------------------

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Remove missing values
df.dropna(inplace=True)

print("\nDataset Information:\n")
print(df.info())

# ---------------------------------
# STEP 3: Basic Analysis
# ---------------------------------

# Total Sales
total_sales = df['sales'].sum()

# Average Sales
average_sales = df['sales'].mean()

print("\n----- SALES ANALYSIS -----")
print("Total Sales:", total_sales)
print("Average Sales:", round(average_sales, 2))

# ---------------------------------
# STEP 4: Identify High Demand Areas
# ---------------------------------

# High demand = High sales and low store presence
high_demand = df[(df['sales'] > df['sales'].mean()) & (df['stores'] <= 2)]

print("\nHigh Demand Areas:\n")
print(high_demand[['region', 'sales', 'stores']])

# ---------------------------------
# STEP 5: Create Map Visualization
# ---------------------------------

# Create map centered around Tamil Nadu
map_center = [11.1271, 78.6569]

business_map = folium.Map(location=map_center, zoom_start=7)

# Add markers
for index, row in df.iterrows():
    
    popup_text = (
        f"Region: {row['region']}<br>"
        f"Sales: {row['sales']}<br>"
        f"Stores: {row['stores']}"
    )

    # Green marker for high demand regions
    if row['region'] in high_demand['region'].values:
        marker_color = 'green'
    else:
        marker_color = 'blue'

    folium.Marker(
        location=[row['latitude'], row['longitude']],
        popup=popup_text,
        icon=folium.Icon(color=marker_color)
    ).add_to(business_map)

# Save map
business_map.save("business_expansion_map.html")

print("\nMap saved successfully as business_expansion_map.html")

# ---------------------------------
# STEP 6: Visualization
# ---------------------------------

# Sales by Region
plt.figure(figsize=(8, 5))
plt.bar(df['region'], df['sales'])
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Stores by Region
plt.figure(figsize=(8, 5))
plt.bar(df['region'], df['stores'])
plt.title("Store Presence by Region")
plt.xlabel("Region")
plt.ylabel("Number of Stores")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------
# STEP 7: Save Cleaned Dataset
# ---------------------------------

df.to_csv("cleaned_geospatial_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
