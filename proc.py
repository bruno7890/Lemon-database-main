import mysql.connector

def GetMaxQuantity(booking_id):
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="little_lemon"
    )

    # Create a cursor
    cursor = connection.cursor()

    # Query the database to retrieve the maximum quantity for the specified booking
    query = f"SELECT MAX(quantity) FROM bookings WHERE booking_id = {booking_id};"
    cursor.execute(query)

    # Fetch the result
    result = cursor.fetchone()
    max_quantity = result[0] if result[0] is not None else 0

    # Close the cursor and the database connection
    cursor.close()
    connection.close()

    return max_quantity
    
    
    import mysql.connector

def ManageBooking(booking_id, action):
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="little_lemon"
    )

    # Create a cursor
    cursor = connection.cursor()

    if action == "CREATE":
        # Create a new booking
        # ...
    elif action == "UPDATE":
        # Update an existing booking
        # ...
    elif action == "CANCEL":
        # Cancel a booking
        # ...
    else:
        # Handle invalid action
        # ...

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()
    
    import mysql.connector

def UpdateBooking(booking_id, new_details):
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="little_lemon"
    )

    # Create a cursor
    cursor = connection.cursor()

    # Update the booking with the new details
    # ...

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()
    
    import mysql.connector

def AddBooking(booking_details):
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="little_lemon"
    )

    # Create a cursor
    cursor = connection.cursor()

    # Add the new booking to the database
    # ...

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()
    
    import mysql.connector

def CancelBooking(booking_id):
    # Connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password",
        database="little_lemon"
    )

    # Create a cursor
    cursor = connection.cursor()

    # Cancel the booking
    # ...

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and the database connection
    cursor.close()
    connection.close()