# TravelIQ Analytics

**Tagline:** Travel & Tourism Business Intelligence Dashboard

---

## 📌 Project Overview
**TravelIQ Analytics** is a comprehensive Data Analytics and Business Intelligence portfolio project. It is designed to analyze travel and tourism data to derive actionable business insights using a robust tech stack, entirely mimicking real-world corporate data workflows.

*Note: This is an analytical BI project, not a booking system or an ML application.*

## 🎯 Objectives
*   Generate highly realistic, rule-based dummy data for the travel sector.
*   Perform extensive Data Cleaning, Transformation, and Feature Engineering using Python (`pandas`, `numpy`).
*   Design a relational database schema and perform deep exploratory data analysis using MySQL.
*   Develop a professional, interactive Business Intelligence dashboard using Power BI to present key insights.

## 🗄️ Dataset Description
The datasets were programmatically generated to simulate realistic business scenarios across 6 key tables:
1.  **Destinations (`destinations.csv`)**: 200 rows containing location data, categories, seasons, ratings, and costs.
2.  **Hotels (`hotels.csv`)**: 500 rows detailing hotel types, prices, occupancy rates, and ratings.
3.  **Tourists (`tourists.csv`)**: 1,000 rows containing demographics, travel types, and budgets.
4.  **Bookings (`bookings.csv`)**: 5,000 rows of transactional data including check-in/out dates, itemized costs, and discounts.
5.  **Reviews (`reviews.csv`)**: 2,000 rows of user reviews with ratings and sentiment analysis.
6.  **Weather (`weather.csv`)**: 1,200 rows covering temperature, humidity, rainfall, and AQI across destinations.

*Business Rules Applied:* Luxury hotels cost more, high-rated hotels maintain higher occupancy, seasonal peaks align with geography (e.g., Goa peaks in December), and family/foreign travelers have higher expenditure profiles.

## 🧹 Cleaning Process (Python)
The `Python/data_cleaning.py` script executes the following ELT pipeline:
*   **Deduplication:** Removed duplicate records across all raw datasets.
*   **Missing Value Imputation:** Filled missing numeric values with medians and categorical values with modes.
*   **Type Casting:** Standardized date formats and numeric types.
*   **Feature Engineering:** Created analytical columns in the `bookings` table, including:
    *   `Stay Duration`
    *   `Revenue` (Total booking cost)
    *   `Profit` (Assuming a 20% margin)
    *   `Average Daily Cost`
    *   `Average Spending` (Aggregated to the tourist level)

## 🗃️ SQL Analysis
A MySQL database (`traveliq`) was constructed using a star schema. Over 50 complex SQL queries were written in `SQL/analysis_queries.sql` to answer analytical questions across 5 categories:
1.  **Destination Analysis:** Popularity, revenue by state, seasonal trends.
2.  **Hotel Analysis:** Luxury vs Budget performance, occupancy vs ratings.
3.  **Tourist Analysis:** Demographic spending habits, travel type distribution.
4.  **Booking & Revenue Analysis:** Monthly revenue growth, discount impact.
5.  **Review & Weather Analysis:** AQI correlation with negative sentiment, seasonal weather impacts.

## 📊 Dashboard Explanation (Power BI)
A 7-page Power BI dashboard blueprint is provided using a dark professional theme with blue accent colors. See `Power BI/dashboard_guide.md` for the layout instructions and suggested DAX measures. A `.pbix` file is not included in this repository.
*   **Page 1: Executive Dashboard** (High-level KPIs, Revenue trends)
*   **Page 2: Destination Analysis** (State-wise popularity, map visuals)
*   **Page 3: Hotel Analysis** (Type vs Occupancy vs Revenue)
*   **Page 4: Tourist Analysis** (Demographics, budget vs actual spend)
*   **Page 5: Booking Analysis** (Seasonality, payment methods)
*   **Page 6: Review Analysis** (Sentiment, top-rated entities)
*   **Page 7: Weather Analysis** (Impact of AQI and rainfall on tourism)

## 💡 Example Findings from the Generated Dataset
Because the data is synthetic and reproducible, findings describe this generated dataset rather than real-world tourism behavior.
*   **Seasonality:** In the current seeded dataset, Monsoon has the highest total generated revenue.
*   **Hotel Occupancy:** Average occupancy is broadly similar across hotel types in the generated data; Resort hotels are highest in the current run.
*   **Peak Demand:** Goa has its highest generated booking volume in December, reflecting a rule intentionally built into the generator.
*   **Demographic Spending:** Family travellers have higher average spending than solo travellers in the current generated dataset.
*   **Weather Analysis:** Weather and review sentiment can be compared with the supplied SQL queries, but the generator does not establish a causal relationship between AQI and sentiment.

## 🚀 Future Scope
*   **Automated Pipeline:** Migrate the Python scripts to a cloud function (e.g., AWS Lambda or GCP Cloud Functions) to automate data ingestion daily.
*   **Advanced Analytics:** Implement predictive forecasting for hotel occupancy and dynamic pricing models.
*   **Live Weather Integration:** Connect a live Weather API to predict short-term booking cancellations.

