\# TravelIQ Analytics: End-to-End Data Pipeline



\## Project Overview

TravelIQ Analytics is an end-to-end data engineering and analytics portfolio project. The goal of this project is to simulate a real-world travel agency's data infrastructure. It demonstrates the ability to generate synthetic datasets, clean and transform data using Python, design a relational database schema in MySQL, and connect a Business Intelligence tool (Power BI) for final dashboarding and insights.



\---



\## Technologies Used

\*   \*\*Python (Pandas, Numpy):\*\* Used for synthetic data generation, data cleaning, handling missing values, and feature engineering (calculating profits, stay durations).

\*   \*\*MySQL:\*\* Used for relational database management. A normalized schema was designed to store the data with strict primary and foreign key constraints to ensure data integrity.

\*   \*\*Power BI:\*\* Used as the frontend Business Intelligence tool to connect directly to the MySQL database, model the data visually, and create interactive dashboards.



\---



\## How It Works (The Pipeline)



The pipeline is broken down into four main stages, represented by the four files in this project:



\### 1. Data Generation (`data\_generation.py`)

Since real travel data is highly confidential, this script generates a robust, simulated dataset from scratch. 

\*   \*\*What it does:\*\* It creates 6 distinct CSV files: `destinations`, `hotels`, `tourists`, `bookings`, `reviews`, and `weather`.

\*   \*\*The Logic:\*\* It uses intelligent randomization to make the data realistic. For example, highly-rated hotels have higher occupancy rates, families have lower budgets than solo foreign travelers, and destinations in Rajasthan receive more bookings in the winter.



\### 2. Data Cleaning \& Transformation (`data\_cleaning.py`)

Raw data is rarely perfect. This script acts as the "ETL" (Extract, Transform, Load) processing step.

\*   \*\*What it does:\*\* It loads the raw CSVs and performs data cleaning operations.

\*   \*\*The Logic:\*\* 

&#x20;   \*   It drops duplicate rows.

&#x20;   \*   It fills missing numeric values with the median and missing text values with the mode.

&#x20;   \*   \*\*Feature Engineering:\*\* It creates entirely new data points that are useful for business analysis. For example, it subtracts the `check\_in` date from the `check\_out` date to calculate `stay\_duration`. It also calculates `profit` (assuming a 20% margin on `total\_cost`).



\### 3. Database Design (`schema.sql`)

Data needs a secure, structured home. This SQL script sets up the database architecture.

\*   \*\*What it does:\*\* It creates a database named `traveliq` and builds 6 tables.

\*   \*\*The Logic:\*\* It defines strict relationships (Foreign Keys). For example, a booking in the `bookings` table MUST be tied to a valid `tourist\_id` from the `tourists` table, and a valid `hotel\_id` from the `hotels` table. This prevents "orphan" records and ensures high data quality. The schema is portable; cleaned CSV files can be imported through MySQL Workbench in the documented foreign-key order.



\### 4. Database Connection (`connect\_database.py`)

This is a utility script to verify the backend is working before moving to Power BI.

\*   \*\*What it does:\*\* It uses the `mysql-connector-python` library to connect to the local MySQL server.

\*   \*\*The Logic:\*\* It reads MySQL connection settings from environment variables, establishes the connection, and runs a small verification query for the top 5 destinations.



\---



\## Business Value \& Meaning

The ultimate goal of this technical pipeline is to allow a Business Analyst to open \*\*Power BI\*\*, connect to the `traveliq` database, and answer critical business questions, such as:



\*   \*\*Profitability Analysis:\*\* Which destination categories (e.g., Beaches vs. Hill Stations) generate the highest average profit margin?

\*   \*\*Customer Segmentation:\*\* Do solo international travelers spend significantly more on activities and shopping compared to domestic families?

\*   \*\*Seasonal Trends:\*\* How does the occupancy rate of luxury hotels fluctuate during the Monsoon season compared to the Winter?

\*   \*\*Sentiment Tracking:\*\* Is there a correlation between negative hotel reviews and specific weather conditions (e.g., high rainfall or AQI)?



By building this infrastructure from the ground up, this project demonstrates a comprehensive understanding of the entire data lifecycle: from generation and cleaning to storage and visualization.





\## Quick Start

1\. Create a virtual environment and install dependencies with `pip install -r requirements.txt`.

2\. Run `python Python/data\_generation.py` to regenerate the raw synthetic datasets.

3\. Run `python Python/data\_cleaning.py` to create the cleaned datasets.

4\. Execute `SQL/schema.sql` in MySQL Workbench, then import the six files from `Data/Cleaned Data` in the order listed in the SQL file.

5\. Set `MYSQL\_HOST`, `MYSQL\_USER`, `MYSQL\_PASSWORD`, and `MYSQL\_DATABASE` (see `.env.example`) and run `python Python/connect\_database.py`.

6\. Run the queries in `SQL/analysis\_queries.sql`; use `Power BI/dashboard\_guide.md` as the dashboard blueprint.



> Note: A Power BI `.pbix` file is not included, so the dashboard design is documented but not bundled as an executable dashboard file.





\## Validation Status

\- Python syntax was checked for all three scripts.

\- `data\_generation.py` and `data\_cleaning.py` were executed successfully and produced the expected six raw and six cleaned datasets.

\- Referential-integrity checks across destination, hotel, tourist, booking, review, and weather IDs passed on the generated CSV data.

\- MySQL execution requires a local MySQL server and credentials, so database import/query execution must be verified on the target machine.

\- The repository contains a Power BI dashboard guide, not a `.pbix` dashboard file.



