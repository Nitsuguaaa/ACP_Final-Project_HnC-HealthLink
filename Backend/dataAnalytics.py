from MySQL03 import sqldir
from collections import Counter
import sqlite3

sql = sqldir.SqlCommands()

class dataAnalysis:
    def topAddress(self):
        addressList = sql.select("patienttbl", "patientAddress")

    def topDisease(self):
        diseaseList = sql.select("patientinfotbl", "patientDisease")

def find_most_common_address():
    # Connect to the SQLite database
    connection = sqlite3.connect("healthlinkdb")  # Replace 'your_database.db' with your actual database file
    cursor = connection.cursor()

    # Execute a query to retrieve all patient addresses
    cursor.execute("patienttbl")  # Replace 'your_table' with your actual table name
    addresses = cursor.fetchall()

    # Close the database connection
    connection.close()

    # Check if there are addresses in the database
    if not addresses:
        print("No addresses found in the database.")
        return

    # Extract the addresses from the result set
    addresses = [addr[0] for addr in addresses]

    # Use Counter to count occurrences of each address
    address_counts = Counter(addresses)

    # Find the most common address
    most_common_address, occurrences = address_counts.most_common(1)[0]

    print("Most Common Address:", most_common_address)
    print("Occurrences:", occurrences)

# Call the function to find and print the most common address
find_most_common_address()