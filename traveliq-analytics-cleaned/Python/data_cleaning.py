import pandas as pd
import numpy as np
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
input_dir = project_root / "Data" / "Raw Data"
output_dir = project_root / "Data" / "Cleaned Data"

output_dir.mkdir(parents=True, exist_ok=True)

print("Starting Data Cleaning Process...")

# 1. Load Data
try:
    df_dest = pd.read_csv(input_dir / "destinations.csv")
    df_hotels = pd.read_csv(input_dir / "hotels.csv")
    df_tourists = pd.read_csv(input_dir / "tourists.csv")
    df_bookings = pd.read_csv(input_dir / "bookings.csv")
    df_reviews = pd.read_csv(input_dir / "reviews.csv")
    df_weather = pd.read_csv(input_dir / "weather.csv")
except Exception as e:
    print(f"Error loading files: {e}")
    exit(1)

# Function to clean dataframe
def clean_dataframe(df, name):
    print(f"Cleaning {name}...")
    # Remove duplicates
    initial_shape = df.shape
    df.drop_duplicates(inplace=True)
    if initial_shape != df.shape:
        print(f"  Removed {initial_shape[0] - df.shape[0]} duplicates.")
    
    # Handle missing values (Fill numeric with median, object with mode)
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype in ['int64', 'float64']:
                df[col] = df[col].fillna(df[col].median())
            else:
                df[col] = df[col].fillna(df[col].mode()[0])
            print(f"  Filled missing values in column '{col}'.")
            
    return df

# 2. Clean Datasets
df_dest = clean_dataframe(df_dest, "Destinations")
df_hotels = clean_dataframe(df_hotels, "Hotels")
df_tourists = clean_dataframe(df_tourists, "Tourists")
df_bookings = clean_dataframe(df_bookings, "Bookings")
df_reviews = clean_dataframe(df_reviews, "Reviews")
df_weather = clean_dataframe(df_weather, "Weather")

# 3. Fix Data Types and Create New Columns

print("Applying Transformations and Feature Engineering...")

# Bookings Transformations
df_bookings['booking_date'] = pd.to_datetime(df_bookings['booking_date'])
df_bookings['check_in'] = pd.to_datetime(df_bookings['check_in'])
df_bookings['check_out'] = pd.to_datetime(df_bookings['check_out'])

# Stay Duration
df_bookings['stay_duration'] = (df_bookings['check_out'] - df_bookings['check_in']).dt.days

# Revenue = total_cost
df_bookings['revenue'] = df_bookings['total_cost']

# Profit (Assuming 20% margin on average across services)
df_bookings['profit'] = round(df_bookings['revenue'] * 0.20, 2)

# Average Daily Cost
df_bookings['average_daily_cost'] = round(df_bookings['revenue'] / df_bookings['stay_duration'].replace(0, 1), 2)

# Tourists Transformations
# Average Spending per tourist (Aggregate from bookings)
tourist_spending = df_bookings.groupby('tourist_id')['total_cost'].mean().reset_index()
tourist_spending.columns = ['tourist_id', 'average_spending']
df_tourists = pd.merge(df_tourists, tourist_spending, on='tourist_id', how='left')
df_tourists['average_spending'] = df_tourists['average_spending'].fillna(0).round(2)

# Reviews Transformations
df_reviews['review_date'] = pd.to_datetime(df_reviews['review_date'])

# Weather Fix Types
df_weather['month'] = df_weather['month'].astype(int)

# 4. Export Cleaned Data
print("Exporting Cleaned Datasets...")
df_dest.to_csv(output_dir / "cleaned_destinations.csv", index=False)
df_hotels.to_csv(output_dir / "cleaned_hotels.csv", index=False)
df_tourists.to_csv(output_dir / "cleaned_tourists.csv", index=False)
df_bookings.to_csv(output_dir / "cleaned_bookings.csv", index=False)
df_reviews.to_csv(output_dir / "cleaned_reviews.csv", index=False)
df_weather.to_csv(output_dir / "cleaned_weather.csv", index=False)

print("Data Cleaning and Transformation Completed Successfully!")
