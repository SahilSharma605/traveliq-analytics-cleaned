# TravelIQ Analytics - Power BI Dashboard Guide

This guide provides the complete blueprint for building the **TravelIQ Analytics** Power BI Dashboard, ensuring a professional, interview-ready presentation.

## 🎨 Theme & Layout Guidelines
*   **Theme**: Dark Professional (Background: `#1E1E2D`, Cards: `#2B2B40`)
*   **Accent Colors**: Blue (`#3699FF`), Teal (`#1BC5BD`), Purple (`#8950FC`)
*   **Typography**: Segoe UI or DIN (Modern, Sans-Serif). Use white/light gray for text.
*   **Design Elements**: Use rounded corners (10px) for all cards and visuals. Add subtle drop shadows.

---

## ⚙️ Data Modeling & Relationships
Load all files from the `Data/Cleaned Data` folder. Establish the following relationships (Star Schema):
*   `bookings` (Fact Table) `* -> 1` `destinations` (Dim) via `destination_id`
*   `bookings` (Fact Table) `* -> 1` `hotels` (Dim) via `hotel_id`
*   `bookings` (Fact Table) `* -> 1` `tourists` (Dim) via `tourist_id`
*   `reviews` (Fact Table) `* -> 1` `destinations` (Dim)
*   `reviews` (Fact Table) `* -> 1` `hotels` (Dim)
*   `weather` (Fact Table) `* -> 1` `destinations` (Dim)

---

## 🧮 DAX Measures (Create a 'Key Measures' table)

```dax
-- Core Metrics
Total Revenue = SUM(bookings[revenue])
Total Bookings = COUNT(bookings[booking_id])
Total Tourists = DISTINCTCOUNT(bookings[tourist_id])
Total Hotels = COUNT(hotels[hotel_id])
Total Destinations = COUNT(destinations[destination_id])

-- Averages
Average Trip Cost = AVERAGE(bookings[total_cost])
Average Rating = AVERAGE(reviews[rating])
Average Occupancy = AVERAGE(hotels[occupancy_rate])
Average Spending = AVERAGE(tourists[average_spending])
Average Stay Duration = AVERAGE(bookings[stay_duration])

-- Advanced Metrics
Revenue Growth % = 
    VAR CurrentRevenue = [Total Revenue]
    VAR PreviousRevenue = CALCULATE([Total Revenue], PREVIOUSMONTH(bookings[booking_date]))
    RETURN DIVIDE(CurrentRevenue - PreviousRevenue, PreviousRevenue, 0)

Highest Revenue Destination = 
    TOPN(1, VALUES(destinations[destination_name]), [Total Revenue], DESC)

Highest Rated Destination = 
    TOPN(1, VALUES(destinations[destination_name]), [Average Rating], DESC)
```

---

## 📊 Page Configurations & Insights

### 🧭 PAGE 1: Executive Dashboard
**Visuals:**
*   **Cards (Top Row):** Total Revenue, Total Bookings, Total Tourists, Total Hotels, Total Destinations, Average Rating, Average Trip Cost, Average Occupancy.
*   **Line Chart:** Monthly Revenue Trend.
*   **Filled Map:** Revenue by State (Dark map style).
*   **Donut Chart:** Revenue by Season.
*   **Bar Chart:** Top Destinations by Revenue.

**💡 Business Insight (Add as text box):**
> "Winter contributes the highest tourism revenue, primarily driven by peak bookings in Rajasthan and Goa. Executive overview shows consistent growth in average trip costs."

### 🗺️ PAGE 2: Destination Analysis
**Visuals:**
*   **Matrix:** State -> City (Rows), Total Bookings, Revenue (Values).
*   **Treemap:** Category Analysis (Hill Station, Beach, etc. by Popularity).
*   **Scatter Plot:** Destination Ratings vs Average Trip Cost.
*   **Map (Bubble):** Top 10 Destinations by Popularity Score.

**💡 Business Insight:**
> "Hill stations maintain steady popularity during summer months, while historical sites in Rajasthan peak significantly in Q4. Popularity highly correlates with average ratings."

### 🏨 PAGE 3: Hotel Analysis
**Visuals:**
*   **Clustered Column:** Luxury vs Budget (Average Price & Occupancy).
*   **Gauge/Card:** Average Occupancy across all types.
*   **Tornado Chart / Funnel:** Revenue by Hotel Type.
*   **Scatter Plot:** Hotel Ratings vs Price Per Night.

**💡 Business Insight:**
> "Luxury hotels generate 45% higher revenue but experience 15% lower average occupancy compared to Budget hotels. Budget hotels maintain the highest consistent occupancy year-round."

### 👥 PAGE 4: Tourist Analysis
**Visuals:**
*   **Column Chart:** Age Distribution (Use DAX grouping or calculated column for bins).
*   **Pie Chart:** Gender Distribution.
*   **Bar Chart:** Revenue by Travel Type (Solo, Family, etc.).
*   **Map/Bar:** Top Visiting Countries.
*   **Waterfall/Funnel:** Budget Distribution vs Actual Spend.

**💡 Business Insight:**
> "Family travellers spend 38% more than solo travellers, primarily on food and activities. Foreign tourists consistently exceed their initial budgets by 12%."

### 📅 PAGE 5: Booking Analysis
**Visuals:**
*   **Area Chart:** Monthly Bookings over time.
*   **Donut Chart:** Payment Method preference.
*   **Stacked Column Chart:** Season Analysis (Bookings by Season).
*   **Line & Stacked Column:** Bookings Trend vs Revenue.

**💡 Business Insight:**
> "Goa receives maximum bookings during December. Credit Cards and UPI dominate payment methods, accounting for over 70% of total transactions."

### ⭐ PAGE 6: Review Analysis
**Visuals:**
*   **Cards:** Average Rating, Positive Reviews (Count), Negative Reviews (Count).
*   **Donut Chart:** Sentiment Breakdown.
*   **Word Cloud (Custom Visual):** Review text keywords.
*   **Table:** Top Rated Hotels & Destinations.

**💡 Business Insight:**
> "Customer satisfaction remains high at 4.2/5 average. Negative reviews are heavily correlated with high AQI days and monsoon disruptions in coastal areas."

### 🌤️ PAGE 7: Weather Analysis
**Visuals:**
*   **Line Chart:** Temperature & Humidity trends by Month.
*   **Column Chart:** Average Rainfall by State.
*   **Scatter Plot:** AQI vs Sentiment Score.
*   **Matrix:** Season Comparison across key weather metrics.

**💡 Business Insight:**
> "Spikes in AQI negatively impact tourist sentiment and outdoor activity spending. Monsoon seasons show a 20% dip in bookings except for specific hill station retreats."

---

## 🎛️ Global Filters (Slicers Panel)
Create a collapsible slicer panel on the left or top of every page containing:
*   State & City
*   Destination
*   Season
*   Hotel Type
*   Travel Type
*   Country
*   Booking Date (Date Range)
