-- ================================================================
-- TravelIQ Analytics - Database Schema
-- ================================================================

CREATE DATABASE IF NOT EXISTS traveliq;
USE traveliq;

-- 1. Destinations Table
CREATE TABLE IF NOT EXISTS destinations (
    destination_id INT PRIMARY KEY,
    destination_name VARCHAR(100),
    city VARCHAR(50),
    state VARCHAR(50),
    category VARCHAR(50),
    best_season VARCHAR(50),
    rating DECIMAL(3, 1),
    entry_fee DECIMAL(10, 2),
    average_trip_cost DECIMAL(10, 2),
    popularity_score DECIMAL(5, 1),
    latitude DECIMAL(10, 4),
    longitude DECIMAL(10, 4)
);

-- 2. Hotels Table
CREATE TABLE IF NOT EXISTS hotels (
    hotel_id INT PRIMARY KEY,
    destination_id INT,
    hotel_name VARCHAR(100),
    hotel_type VARCHAR(50),
    price_per_night DECIMAL(10, 2),
    hotel_rating DECIMAL(3, 1),
    occupancy_rate DECIMAL(5, 1),
    rooms INT,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

-- 3. Tourists Table
CREATE TABLE IF NOT EXISTS tourists (
    tourist_id INT PRIMARY KEY,
    age INT,
    gender VARCHAR(20),
    country VARCHAR(50),
    travel_type VARCHAR(50),
    budget DECIMAL(12, 2),
    average_spending DECIMAL(12, 2)
);

-- 4. Bookings Table
CREATE TABLE IF NOT EXISTS bookings (
    booking_id INT PRIMARY KEY,
    tourist_id INT,
    hotel_id INT,
    destination_id INT,
    booking_date DATE,
    check_in DATE,
    check_out DATE,
    season VARCHAR(20),
    payment_method VARCHAR(50),
    hotel_cost DECIMAL(10, 2),
    food_cost DECIMAL(10, 2),
    transport_cost DECIMAL(10, 2),
    shopping_cost DECIMAL(10, 2),
    activity_cost DECIMAL(10, 2),
    discount DECIMAL(10, 2),
    total_cost DECIMAL(10, 2),
    stay_duration INT,
    revenue DECIMAL(10, 2),
    profit DECIMAL(10, 2),
    average_daily_cost DECIMAL(10, 2),
    FOREIGN KEY (tourist_id) REFERENCES tourists(tourist_id),
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id),
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

-- 5. Reviews Table
CREATE TABLE IF NOT EXISTS reviews (
    review_id INT PRIMARY KEY,
    destination_id INT,
    hotel_id INT,
    rating DECIMAL(3, 1),
    sentiment VARCHAR(20),
    review TEXT,
    review_date DATE,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id),
    FOREIGN KEY (hotel_id) REFERENCES hotels(hotel_id)
);

-- 6. Weather Table
CREATE TABLE IF NOT EXISTS weather (
    destination_id INT,
    month INT,
    temperature DECIMAL(5, 1),
    humidity INT,
    rainfall DECIMAL(5, 1),
    aqi INT,
    FOREIGN KEY (destination_id) REFERENCES destinations(destination_id)
);

-- ================================================================
-- Data Import
-- ================================================================
-- After creating the schema, import the cleaned CSV files from
-- Data/Cleaned Data using MySQL Workbench's Table Data Import Wizard.
-- Import in this order to satisfy foreign keys:
-- 1. cleaned_destinations.csv
-- 2. cleaned_hotels.csv
-- 3. cleaned_tourists.csv
-- 4. cleaned_bookings.csv
-- 5. cleaned_reviews.csv
-- 6. cleaned_weather.csv
