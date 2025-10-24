#!/usr/bin/python3
"""
Script that creates a MySQL database named alx_book_store.
If it already exists, the script will not fail.
"""

import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL Server (update password if needed)
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='#Mrantwi&kwame1'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store;")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()

