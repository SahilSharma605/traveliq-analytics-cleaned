import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
from pathlib import Path

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

# Resolve paths relative to the project so this works from any terminal location
project_root = Path(__file__).resolve().parent.parent
output_dir = project_root / "Data" / "Raw Data"
output_dir.mkdir(parents=True, exist_ok=True)

print("Starting Data Generation...")

# ---------------------------------------------------------
# 1. destinations.csv (200 rows)
# ---------------------------------------------------------
states = {
    'Rajasthan': ['Jaipur', 'Udaipur', 'Jodhpur', 'Jaisalmer', 'Pushkar'],
    'Goa': ['Panaji', 'Vasco da Gama', 'Margao', 'Mapusa', 'Calangute'],
    'Kerala': ['Munnar', 'Kochi', 'Alleppey', 'Wayanad', 'Trivandrum'],
    'Himachal Pradesh': ['Shimla', 'Manali', 'Dharamshala', 'Dalhousie', 'Kasauli'],
    'Uttarakhand': ['Nainital', 'Mussoorie', 'Rishikesh', 'Haridwar', 'Dehradun'],
    'Maharashtra': ['Mumbai', 'Pune', 'Mahabaleshwar', 'Lonavala', 'Nashik'],
    'Tamil Nadu': ['Ooty', 'Kodaikanal', 'Chennai', 'Madurai', 'Coimbatore'],
    'Karnataka': ['Bangalore', 'Mysore', 'Coorg', 'Hampi', 'Gokarna']
}

categories = ['Hill Station', 'Beach', 'Historical', 'Adventure', 'Pilgrimage', 'Nature']

destinations_data = []
for i in range(1, 201):
    state = random.choice(list(states.keys()))
    city = random.choice(states[state])
    dest_name = f"{city} {random.choice(['Valley', 'Fort', 'Beach', 'Temple', 'Resort', 'Point', 'Lake'])}"
    
    category = 'Historical' if state == 'Rajasthan' else 'Beach' if state == 'Goa' else 'Hill Station' if state in ['Himachal Pradesh', 'Uttarakhand'] else random.choice(categories)
    
    best_season = 'Winter' if state == 'Rajasthan' else 'Summer' if category == 'Hill Station' else random.choice(['Winter', 'Summer', 'Monsoon', 'All Season'])
    
    rating = round(random.uniform(3.5, 5.0), 1)
    entry_fee = round(random.uniform(0, 500), 2)
    avg_trip_cost = round(random.uniform(5000, 20000), 2)
    popularity_score = round(random.uniform(50, 100), 1)
    
    lat = round(random.uniform(8.0, 37.0), 4)
    lon = round(random.uniform(68.0, 97.0), 4)
    
    destinations_data.append([i, dest_name, city, state, category, best_season, rating, entry_fee, avg_trip_cost, popularity_score, lat, lon])

df_destinations = pd.DataFrame(destinations_data, columns=['destination_id', 'destination_name', 'city', 'state', 'category', 'best_season', 'rating', 'entry_fee', 'average_trip_cost', 'popularity_score', 'latitude', 'longitude'])
df_destinations.to_csv(output_dir / "destinations.csv", index=False)
print("Created destinations.csv")

# ---------------------------------------------------------
# 2. hotels.csv (500 rows)
# ---------------------------------------------------------
hotel_types = ['Luxury', 'Standard', 'Budget', 'Resort', 'Homestay']

hotels_data = []
for i in range(1, 501):
    dest_id = random.randint(1, 200)
    hotel_type = random.choices(hotel_types, weights=[15, 35, 30, 15, 5])[0]
    hotel_name = f"{random.choice(['Grand', 'Royal', 'Sea', 'Mountain', 'Silver', 'Golden', 'Sunset'])} {random.choice(['Inn', 'Hotel', 'Resort', 'Retreat', 'Lodge'])}"
    
    # Luxury hotels cost more, budget less
    if hotel_type == 'Luxury':
        price = round(random.uniform(8000, 25000), 2)
    elif hotel_type == 'Resort':
        price = round(random.uniform(5000, 15000), 2)
    elif hotel_type == 'Standard':
        price = round(random.uniform(2000, 6000), 2)
    else: # Budget / Homestay
        price = round(random.uniform(800, 2500), 2)
        
    rating = round(random.uniform(3.5, 5.0), 1)
    
    # Highly rated hotels have higher occupancy (between 45% and 98%)
    base_occ = 45 + ((rating - 3.5) / 1.5) * 40 # Maps 3.5-5.0 to approx 45-85
    occupancy = round(min(98.0, max(45.0, base_occ + random.uniform(-5, 13))), 1)
    
    rooms = random.randint(20, 200)
    
    hotels_data.append([i, dest_id, hotel_name, hotel_type, price, rating, occupancy, rooms])

df_hotels = pd.DataFrame(hotels_data, columns=['hotel_id', 'destination_id', 'hotel_name', 'hotel_type', 'price_per_night', 'hotel_rating', 'occupancy_rate', 'rooms'])
df_hotels.to_csv(output_dir / "hotels.csv", index=False)
print("Created hotels.csv")

# ---------------------------------------------------------
# 3. tourists.csv (1000 rows)
# ---------------------------------------------------------
countries = ['India', 'USA', 'UK', 'Australia', 'Germany', 'France', 'Canada', 'Japan', 'UAE', 'Singapore']
travel_types = ['Solo', 'Couple', 'Family', 'Friends', 'Business']

tourists_data = []
for i in range(1, 1001):
    age = random.randint(18, 75)
    gender = random.choice(['Male', 'Female'])
    # 70% Indian, 30% Foreign
    country = random.choices(countries, weights=[70, 5, 5, 5, 3, 3, 3, 2, 2, 2])[0]
    
    travel_type = random.choices(travel_types, weights=[15, 30, 35, 15, 5])[0]
    
    # Budget assignment based on country and travel type
    if country != 'India':
        budget = round(random.uniform(50000, 150000), 2)
    else:
        if travel_type == 'Family':
            budget = round(random.uniform(30000, 80000), 2)
        else:
            budget = round(random.uniform(10000, 40000), 2)
            
    tourists_data.append([i, age, gender, country, travel_type, budget])

df_tourists = pd.DataFrame(tourists_data, columns=['tourist_id', 'age', 'gender', 'country', 'travel_type', 'budget'])
df_tourists.to_csv(output_dir / "tourists.csv", index=False)
print("Created tourists.csv")

# ---------------------------------------------------------
# 4. bookings.csv (5000 rows)
# ---------------------------------------------------------
seasons = ['Winter', 'Summer', 'Monsoon', 'Spring', 'Autumn']
payment_methods = ['Credit Card', 'Debit Card', 'UPI', 'Net Banking', 'Cash']

# Helpers to determine season
def get_season(month):
    if month in [12, 1, 2]: return 'Winter'
    if month in [3, 4, 5]: return 'Summer'
    if month in [6, 7, 8]: return 'Monsoon'
    return 'Autumn'

bookings_data = []
start_date = datetime(2023, 1, 1)

for i in range(1, 5001):
    tourist = df_tourists.iloc[random.randint(0, 999)]
    hotel = df_hotels.iloc[random.randint(0, 499)]
    dest = df_destinations[df_destinations['destination_id'] == hotel['destination_id']].iloc[0]
    
    # Logic for month based on rules:
    # Hill stations popular in summer
    # Rajasthan popular in winter
    # Goa receives highest bookings during December
    
    month_weights = [1]*12
    if dest['state'] == 'Goa':
        month_weights[11] = 10 # Dec
    elif dest['state'] == 'Rajasthan':
        month_weights[10] = 5 # Nov
        month_weights[11] = 5 # Dec
        month_weights[0] = 5  # Jan
        month_weights[1] = 5  # Feb
    elif dest['category'] == 'Hill Station':
        month_weights[4] = 5  # May
        month_weights[5] = 5  # Jun
        month_weights[6] = 5  # Jul
        
    month = random.choices(range(1, 13), weights=month_weights)[0]
    year = random.choice([2023, 2024])
    day = random.randint(1, 28)
    
    booking_date = datetime(year, month, day) - timedelta(days=random.randint(5, 60))
    check_in = datetime(year, month, day)
    stay_duration = random.randint(2, 7)
    check_out = check_in + timedelta(days=stay_duration)
    
    season = get_season(month)
    payment_method = random.choice(payment_methods)
    
    # Costs
    hotel_cost = round(hotel['price_per_night'] * stay_duration, 2)
    
    # Family travellers spend more, Foreign tourists spend more
    multiplier = 1.0
    if tourist['travel_type'] == 'Family': multiplier *= 1.8
    if tourist['country'] != 'India': multiplier *= 2.0
    
    food_cost = round(random.uniform(500, 2000) * stay_duration * multiplier, 2)
    transport_cost = round(random.uniform(1000, 5000) * multiplier, 2)
    shopping_cost = round(random.uniform(0, 10000) * multiplier, 2)
    activity_cost = round(random.uniform(500, 4000) * multiplier, 2)
    
    discount = round(random.uniform(0, 0.15) * hotel_cost, 2)
    total_cost = round(hotel_cost + food_cost + transport_cost + shopping_cost + activity_cost - discount, 2)
    
    bookings_data.append([
        i, tourist['tourist_id'], hotel['hotel_id'], dest['destination_id'],
        booking_date.strftime('%Y-%m-%d'), check_in.strftime('%Y-%m-%d'), check_out.strftime('%Y-%m-%d'),
        season, payment_method, hotel_cost, food_cost, transport_cost, shopping_cost, activity_cost, discount, total_cost
    ])

df_bookings = pd.DataFrame(bookings_data, columns=[
    'booking_id', 'tourist_id', 'hotel_id', 'destination_id', 'booking_date', 'check_in', 'check_out',
    'season', 'payment_method', 'hotel_cost', 'food_cost', 'transport_cost', 'shopping_cost', 'activity_cost', 'discount', 'total_cost'
])
df_bookings.to_csv(output_dir / "bookings.csv", index=False)
print("Created bookings.csv")

# ---------------------------------------------------------
# 5. reviews.csv (2000 rows)
# ---------------------------------------------------------
reviews_data = []
for i in range(1, 2001):
    # Popular destinations receive more reviews
    # We will pick from bookings to ensure consistency
    booking = df_bookings.iloc[random.randint(0, 4999)]
    dest_id = booking['destination_id']
    hotel_id = booking['hotel_id']
    
    # Base rating on hotel rating with some variance
    hotel = df_hotels[df_hotels['hotel_id'] == hotel_id].iloc[0]
    rating = round(min(5.0, max(1.0, hotel['hotel_rating'] + random.uniform(-1, 0.5))), 1)
    
    if rating >= 4.0:
        sentiment = 'Positive'
        review_texts = ['Great experience!', 'Loved the stay.', 'Highly recommended.', 'Beautiful place.', 'Excellent service!']
    elif rating >= 3.0:
        sentiment = 'Neutral'
        review_texts = ['It was okay.', 'Average experience.', 'Could be better.', 'Decent place.']
    else:
        sentiment = 'Negative'
        review_texts = ['Terrible experience.', 'Not recommended at all.', 'Very disappointed.', 'Bad service.']
        
    review = random.choice(review_texts)
    
    # Date should be after check_out
    check_out_date = datetime.strptime(booking['check_out'], '%Y-%m-%d')
    review_date = check_out_date + timedelta(days=random.randint(1, 30))
    
    reviews_data.append([i, dest_id, hotel_id, rating, sentiment, review, review_date.strftime('%Y-%m-%d')])

df_reviews = pd.DataFrame(reviews_data, columns=['review_id', 'destination_id', 'hotel_id', 'rating', 'sentiment', 'review', 'review_date'])
df_reviews.to_csv(output_dir / "reviews.csv", index=False)
print("Created reviews.csv")

# ---------------------------------------------------------
# 6. weather.csv (1200 rows)
# ---------------------------------------------------------
weather_data = []
id_counter = 1
for dest_id in df_destinations['destination_id'].unique():
    # Only need 6 months? Or 1200 total, which is exactly 200 destinations * 6 months. Wait, requirement says 1200 rows.
    # We have 200 destinations. So 6 months? Let's just do random 6 months or 1 to 6.
    # Let's do month 1 to 6 for each destination to get exactly 1200 rows.
    for month in range(1, 7):
        # generate reasonable weather
        dest = df_destinations[df_destinations['destination_id'] == dest_id].iloc[0]
        if dest['category'] == 'Hill Station':
            temp = round(random.uniform(5, 20), 1)
            humidity = random.randint(40, 70)
        elif dest['state'] == 'Rajasthan':
            temp = round(random.uniform(15, 45), 1)
            humidity = random.randint(20, 50)
        else:
            temp = round(random.uniform(25, 35), 1)
            humidity = random.randint(60, 90)
            
        rainfall = round(random.uniform(0, 200), 1)
        aqi = random.randint(30, 200)
        
        weather_data.append([dest_id, month, temp, humidity, rainfall, aqi])
        id_counter += 1
        
        if len(weather_data) == 1200:
            break
    if len(weather_data) == 1200:
        break

df_weather = pd.DataFrame(weather_data, columns=['destination_id', 'month', 'temperature', 'humidity', 'rainfall', 'aqi'])
df_weather.to_csv(output_dir / "weather.csv", index=False)
print("Created weather.csv")

print("All datasets generated successfully!")
