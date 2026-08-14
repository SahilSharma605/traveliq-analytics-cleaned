"""Verify that the TravelIQ MySQL database is reachable and queryable."""

import os
import mysql.connector

DB_CONFIG = {
    "host": os.getenv("MYSQL_HOST", "localhost"),
    "user": os.getenv("MYSQL_USER", "root"),
    "password": os.getenv("MYSQL_PASSWORD", ""),
    "database": os.getenv("MYSQL_DATABASE", "traveliq"),
}

def main():
    connection = None
    try:
        print(f"Connecting to MySQL database '{DB_CONFIG['database']}' on {DB_CONFIG['host']}...")
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor()
        cursor.execute("""
            SELECT destination_name, city, category, popularity_score
            FROM destinations
            ORDER BY popularity_score DESC
            LIMIT 5
        """)
        print("\nTop 5 destinations by popularity score:")
        print("destination_name | city | category | popularity_score")
        for row in cursor.fetchall():
            print(" | ".join(str(value) for value in row))
        cursor.close()
        print("\nDatabase connection test completed successfully.")
    except mysql.connector.Error as exc:
        print(f"MySQL connection/query failed: {exc}")
        print("Check the MYSQL_* environment variables and confirm that schema.sql was loaded.")
        raise SystemExit(1)
    finally:
        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    main()
