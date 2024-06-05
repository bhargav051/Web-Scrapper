import psycopg2
import CRUD
from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

user=os.getenv('user')
password=os.getenv('password')
host=os.getenv('host')
port=os.getenv('port')
database=os.getenv('database')

def create_table():
    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Winning_team (
                "Year" text,
                "Winner" text,
                "Hosting country" text,
                "Runner-up" text
            );
        """)

        # Commit the changes
        connection.commit()

    except (Exception, psycopg2.Error) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Create the table (if not already done)
create_table()

# function to insert the data manualy
def insert_data():
    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

        cursor = connection.cursor()

        year = input("Enter the year: ")
        winner = input("Enter the winner: ")
        hosting_country = input("Enter the hosting country: ")
        runner_up = input("Enter the runner-up: ")

        cursor.execute("""
            INSERT INTO Winning_team ("Year", "Winner", "Hosting country", "Runner-up")
            VALUES (%s, %s, %s, %s);
        """, (year, winner, hosting_country, runner_up))

        # Commit the changes
        connection.commit()
        print("Data inserted successfully!")

    except (Exception, psycopg2.Error) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# creating the database using the data scraped by the crawler
def insert_data_into_db(data):
    try:
        # Connect to the PostgreSQL server
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        print("Database 'Cricket_worldcup_winner' connected successfully!")

        # Create a cursor
        cursor = connection.cursor()

# Create the table if it doesn't exist
        create_table_query = """
        CREATE TABLE IF NOT EXISTS Winning_team (
            "Year" text,
            "Winner" text,
            "Hosting country" text,
            "Runner-up" text
        );
        """
        cursor.execute(create_table_query)
        connection.commit()

        # Insert data into the table
        insert_query = """
        INSERT INTO Winning_team ("Year", "Winner", "Hosting country", "Runner-up")
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(insert_query, data)
        connection.commit()

        print("Data inserted successfully!")

    except (Exception, psycopg2.Error) as error:
        print(f"Error: {error}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()
            print("Connection closed.")

# Call the fetch_data function
CRUD.fetch_data()

# Example usage: Delete the row with year "2011"
CRUD.delete_row_by_year("1999")

# Call the fetch_data function
CRUD.fetch_data()

# Example usage: Update the winner for year "2011" to "India"
CRUD.edit_winner_by_year("1992", "India")

# Call the fetch_data function
CRUD.fetch_data()



