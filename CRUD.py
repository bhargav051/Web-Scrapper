import psycopg2
from dotenv import load_dotenv
import os

BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, '.env'))

user=os.getenv('user')
password=os.getenv('password')
host=os.getenv('host')
port=os.getenv('port')
database=os.getenv('database')

# Reading the data from the database
def fetch_data():
    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

        cursor = connection.cursor()

        # Execute a SELECT query to fetch data from the table
        cursor.execute("SELECT * FROM Winning_team")

        # Fetch all rows
        rows = cursor.fetchall()

        # Print the data
        for row in rows:
            print(row)

    except (Exception, psycopg2.Error) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# function to delete a particular row

def delete_row_by_year(year_to_delete):
    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

        cursor = connection.cursor()

        # Execute a DELETE query to remove the row with the specified year
        cursor.execute("DELETE FROM Winning_team WHERE \"Year\" = %s", (year_to_delete,))

        # Commit the changes
        connection.commit()
        print(f"Row with year {year_to_delete} deleted successfully!")

    except (Exception, psycopg2.Error) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# function to edit a row

def edit_winner_by_year(year_to_edit, new_winner):
    try:
        connection = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )

        cursor = connection.cursor()

        # Execute an UPDATE query to modify the winner for the specified year
        cursor.execute("UPDATE Winning_team SET \"Winner\" = %s WHERE \"Year\" = %s", (new_winner, year_to_edit))

        # Commit the changes
        connection.commit()
        print(f"Winner for year {year_to_edit} updated to {new_winner} successfully!")

    except (Exception, psycopg2.Error) as e:
        print(f"Error: {e}")

    finally:
        # Close the cursor and connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

