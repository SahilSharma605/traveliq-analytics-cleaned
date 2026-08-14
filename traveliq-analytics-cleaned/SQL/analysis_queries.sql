-- ================================================================
-- TravelIQ Analytics - Analysis Queries (50 Queries)
-- ================================================================

USE traveliq;

-- ----------------------------------------------------------------
-- CATEGORY 1: DESTINATION ANALYSIS
-- ----------------------------------------------------------------

-- 1. Top 10 most popular destinations
SELECT destination_name, state, popularity_score 
FROM destinations 
ORDER BY popularity_score DESC LIMIT 10;

-- 2. Top revenue generating states
SELECT d.state, SUM(b.revenue) as total_revenue
FROM bookings b
JOIN destinations d ON b.destination_id = d.destination_id
GROUP BY d.state
ORDER BY total_revenue DESC;

-- 3. Number of destinations by category
SELECT category, COUNT(*) as destination_count
FROM destinations
GROUP BY category
ORDER BY destination_count DESC;

-- 4. Highest rated destinations
SELECT destination_name, state, rating
FROM destinations
ORDER BY rating DESC LIMIT 10;

-- 5. Average trip cost by state
SELECT state, ROUND(AVG(average_trip_cost), 2) as avg_cost
FROM destinations
GROUP BY state
ORDER BY avg_cost DESC;

-- 6. Revenue by destination
SELECT d.destination_name, SUM(b.revenue) as total_revenue
FROM bookings b
JOIN destinations d ON b.destination_id = d.destination_id
GROUP BY d.destination_name
ORDER BY total_revenue DESC LIMIT 10;

-- 7. Destinations with the highest entry fee
SELECT destination_name, entry_fee 
FROM destinations 
ORDER BY entry_fee DESC LIMIT 5;

-- 8. Destinations popular in Winter
SELECT destination_name, state, popularity_score
FROM destinations
WHERE best_season = 'Winter'
ORDER BY popularity_score DESC LIMIT 10;

-- 9. State-wise average popularity score
SELECT state, ROUND(AVG(popularity_score), 2) as avg_popularity
FROM destinations
GROUP BY state
ORDER BY avg_popularity DESC;

-- 10. Most visited city (by number of bookings)
SELECT d.city, COUNT(b.booking_id) as total_visits
FROM bookings b
JOIN destinations d ON b.destination_id = d.destination_id
GROUP BY d.city
ORDER BY total_visits DESC LIMIT 1;


-- ----------------------------------------------------------------
-- CATEGORY 2: HOTEL ANALYSIS
-- ----------------------------------------------------------------

-- 11. Most booked hotels
SELECT h.hotel_name, COUNT(b.booking_id) as total_bookings
FROM bookings b
JOIN hotels h ON b.hotel_id = h.hotel_id
GROUP BY h.hotel_name
ORDER BY total_bookings DESC LIMIT 10;

-- 12. Top hotel ratings
SELECT hotel_name, hotel_rating, hotel_type
FROM hotels
ORDER BY hotel_rating DESC LIMIT 10;

-- 13. Average price per night by hotel type
SELECT hotel_type, ROUND(AVG(price_per_night), 2) as avg_price
FROM hotels
GROUP BY hotel_type
ORDER BY avg_price DESC;

-- 14. Average occupancy rate by hotel type
SELECT hotel_type, ROUND(AVG(occupancy_rate), 2) as avg_occupancy
FROM hotels
GROUP BY hotel_type
ORDER BY avg_occupancy DESC;

-- 15. Luxury vs Budget hotel revenue comparison
SELECT h.hotel_type, SUM(b.revenue) as total_revenue
FROM bookings b
JOIN hotels h ON b.hotel_id = h.hotel_id
WHERE h.hotel_type IN ('Luxury', 'Budget')
GROUP BY h.hotel_type;

-- 16. Hotels with highest occupancy but low rating (< 4.0)
SELECT hotel_name, occupancy_rate, hotel_rating
FROM hotels
WHERE hotel_rating < 4.0
ORDER BY occupancy_rate DESC LIMIT 10;

-- 17. Total rooms available by destination state
SELECT d.state, SUM(h.rooms) as total_rooms
FROM hotels h
JOIN destinations d ON h.destination_id = d.destination_id
GROUP BY d.state
ORDER BY total_rooms DESC;

-- 18. Hotels generating the most profit
SELECT h.hotel_name, SUM(b.profit) as total_profit
FROM bookings b
JOIN hotels h ON b.hotel_id = h.hotel_id
GROUP BY h.hotel_name
ORDER BY total_profit DESC LIMIT 10;

-- 19. Average stay duration by hotel type
SELECT h.hotel_type, ROUND(AVG(b.stay_duration), 2) as avg_stay
FROM bookings b
JOIN hotels h ON b.hotel_id = h.hotel_id
GROUP BY h.hotel_type
ORDER BY avg_stay DESC;

-- 20. Total discount given by hotel type
SELECT h.hotel_type, SUM(b.discount) as total_discount
FROM bookings b
JOIN hotels h ON b.hotel_id = h.hotel_id
GROUP BY h.hotel_type
ORDER BY total_discount DESC;


-- ----------------------------------------------------------------
-- CATEGORY 3: TOURIST ANALYSIS
-- ----------------------------------------------------------------

-- 21. Tourist age groups (Under 30, 30-50, Over 50)
SELECT 
    CASE 
        WHEN age < 30 THEN 'Under 30'
        WHEN age BETWEEN 30 AND 50 THEN '30-50'
        ELSE 'Over 50' 
    END AS age_group,
    COUNT(*) as total_tourists
FROM tourists
GROUP BY age_group;

-- 22. Country analysis (Top visiting countries)
SELECT country, COUNT(*) as total_tourists
FROM tourists
GROUP BY country
ORDER BY total_tourists DESC;

-- 23. Average spending by country
SELECT country, ROUND(AVG(average_spending), 2) as avg_spend
FROM tourists
GROUP BY country
ORDER BY avg_spend DESC;

-- 24. Budget vs Average Spending (Are tourists overspending?)
SELECT tourist_id, budget, average_spending, (average_spending - budget) as overspend
FROM tourists
WHERE average_spending > budget
ORDER BY overspend DESC LIMIT 10;

-- 25. Travel type analysis (Solo vs Family etc.)
SELECT travel_type, COUNT(*) as count
FROM tourists
GROUP BY travel_type
ORDER BY count DESC;

-- 26. Average spending by travel type
SELECT travel_type, ROUND(AVG(average_spending), 2) as avg_spend
FROM tourists
GROUP BY travel_type
ORDER BY avg_spend DESC;

-- 27. Gender distribution of tourists
SELECT gender, COUNT(*) as count
FROM tourists
GROUP BY gender;

-- 28. Most popular travel type for foreign tourists
SELECT travel_type, COUNT(*) as count
FROM tourists
WHERE country != 'India'
GROUP BY travel_type
ORDER BY count DESC;

-- 29. Total revenue by tourist gender
SELECT t.gender, SUM(b.revenue) as total_revenue
FROM bookings b
JOIN tourists t ON b.tourist_id = t.tourist_id
GROUP BY t.gender;

-- 30. Top 10 highest spending tourists
SELECT t.tourist_id, t.country, t.travel_type, SUM(b.total_cost) as total_spent
FROM bookings b
JOIN tourists t ON b.tourist_id = t.tourist_id
GROUP BY t.tourist_id, t.country, t.travel_type
ORDER BY total_spent DESC LIMIT 10;


-- ----------------------------------------------------------------
-- CATEGORY 4: BOOKING & REVENUE ANALYSIS
-- ----------------------------------------------------------------

-- 31. Monthly revenue
SELECT MONTH(booking_date) as month, SUM(revenue) as total_revenue
FROM bookings
GROUP BY MONTH(booking_date)
ORDER BY month;

-- 32. Revenue by season
SELECT season, SUM(revenue) as total_revenue
FROM bookings
GROUP BY season
ORDER BY total_revenue DESC;

-- 33. Average trip cost (overall)
SELECT ROUND(AVG(total_cost), 2) as avg_trip_cost
FROM bookings;

-- 34. Payment method popularity
SELECT payment_method, COUNT(*) as usage_count
FROM bookings
GROUP BY payment_method
ORDER BY usage_count DESC;

-- 35. Revenue growth (Year over Year if applicable, else month over month)
SELECT YEAR(booking_date) as year, MONTH(booking_date) as month, SUM(revenue) as revenue
FROM bookings
GROUP BY YEAR(booking_date), MONTH(booking_date)
ORDER BY year, month;

-- 36. Average stay duration across all bookings
SELECT ROUND(AVG(stay_duration), 2) as avg_stay_duration
FROM bookings;

-- 37. Highest booking month for Goa
SELECT MONTH(b.booking_date) as month, COUNT(*) as total_bookings
FROM bookings b
JOIN destinations d ON b.destination_id = d.destination_id
WHERE d.state = 'Goa'
GROUP BY MONTH(b.booking_date)
ORDER BY total_bookings DESC LIMIT 1;

-- 38. Total food vs transport vs shopping cost
SELECT 
    SUM(food_cost) as total_food, 
    SUM(transport_cost) as total_transport, 
    SUM(shopping_cost) as total_shopping
FROM bookings;

-- 39. Average daily cost by season
SELECT season, ROUND(AVG(average_daily_cost), 2) as avg_daily_cost
FROM bookings
GROUP BY season
ORDER BY avg_daily_cost DESC;

-- 40. Bookings with highest discount percentage
SELECT booking_id, hotel_cost, discount, ROUND((discount/hotel_cost)*100, 2) as discount_pct
FROM bookings
WHERE hotel_cost > 0
ORDER BY discount_pct DESC LIMIT 10;


-- ----------------------------------------------------------------
-- CATEGORY 5: REVIEWS & WEATHER ANALYSIS
-- ----------------------------------------------------------------

-- 41. Sentiment distribution
SELECT sentiment, COUNT(*) as count
FROM reviews
GROUP BY sentiment;

-- 42. Average review rating by destination category
SELECT d.category, ROUND(AVG(r.rating), 2) as avg_rating
FROM reviews r
JOIN destinations d ON r.destination_id = d.destination_id
GROUP BY d.category
ORDER BY avg_rating DESC;

-- 43. Hotels with the most negative reviews
SELECT h.hotel_name, COUNT(*) as negative_reviews
FROM reviews r
JOIN hotels h ON r.hotel_id = h.hotel_id
WHERE r.sentiment = 'Negative'
GROUP BY h.hotel_name
ORDER BY negative_reviews DESC LIMIT 10;

-- 44. Average temperature by destination state
SELECT d.state, ROUND(AVG(w.temperature), 2) as avg_temp
FROM weather w
JOIN destinations d ON w.destination_id = d.destination_id
GROUP BY d.state;

-- 45. Weather impact: Average rainfall by month
SELECT month, ROUND(AVG(rainfall), 2) as avg_rainfall
FROM weather
GROUP BY month
ORDER BY month;

-- 46. Destinations with highest average AQI
SELECT d.destination_name, ROUND(AVG(w.aqi), 2) as avg_aqi
FROM weather w
JOIN destinations d ON w.destination_id = d.destination_id
GROUP BY d.destination_name
ORDER BY avg_aqi DESC LIMIT 10;

-- 47. Correlation proxy: High AQI and Negative Reviews (Count)
SELECT d.destination_name, AVG(w.aqi) as avg_aqi, 
       (SELECT COUNT(*) FROM reviews r WHERE r.destination_id = d.destination_id AND r.sentiment = 'Negative') as negative_reviews
FROM weather w
JOIN destinations d ON w.destination_id = d.destination_id
GROUP BY d.destination_id, d.destination_name
HAVING avg_aqi > 100
ORDER BY negative_reviews DESC LIMIT 10;

-- 48. Top 5 destinations reviewed favorably (Rating >= 4.5)
SELECT d.destination_name, COUNT(*) as positive_reviews
FROM reviews r
JOIN destinations d ON r.destination_id = d.destination_id
WHERE r.rating >= 4.5
GROUP BY d.destination_name
ORDER BY positive_reviews DESC LIMIT 5;

-- 49. Average hotel rating vs average review rating (Data Consistency Check)
SELECT h.hotel_name, h.hotel_rating, ROUND(AVG(r.rating), 2) as avg_user_rating
FROM hotels h
JOIN reviews r ON h.hotel_id = r.hotel_id
GROUP BY h.hotel_id, h.hotel_name
ORDER BY ABS(h.hotel_rating - AVG(r.rating)) DESC LIMIT 10;

-- 50. Coldest destinations (Min temperature)
SELECT d.destination_name, d.state, MIN(w.temperature) as min_temp
FROM weather w
JOIN destinations d ON w.destination_id = d.destination_id
GROUP BY d.destination_id, d.destination_name, d.state
ORDER BY min_temp ASC LIMIT 10;
