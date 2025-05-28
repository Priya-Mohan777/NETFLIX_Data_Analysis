import pandas as pd

# Load dataset
data = pd.read_csv("NETFLIX.csv")

# Display the top 5 rows
print(data.head(5))

# Show data info
data.info()

# Get column names
print(data.columns)

# Drop unwanted unnamed columns
data.drop(columns=[
    'Unnamed: 12', 'Unnamed: 13', 'Unnamed: 14', 'Unnamed: 15',
    'Unnamed: 16', 'Unnamed: 17', 'Unnamed: 18', 'Unnamed: 19',
    'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23',
    'Unnamed: 24', 'Unnamed: 25'
], inplace=True, errors='ignore')

# Capitalize first letter of each column
data.columns = [col.capitalize() for col in data.columns]

# Check for duplicates
print("Duplicate rows:", data.duplicated().sum())

# Remove duplicates
data.drop_duplicates(inplace=True)

# Check null values
print("Nulls:\n", data.isna().sum())

# Fill missing values
data.fillna({
    "Director": "missing",
    "Cast": "Unknown",
    "Country": "Unknown"
}, inplace=True)

# Final check
print("After cleaning:\n", data.info())
