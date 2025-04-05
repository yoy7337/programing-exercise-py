import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect('user_order.sqlite')

# Create a cursor object
cur = conn.cursor()

def main():
    # Query 1: Select all users
    print(">>> pd.read_sql_query('SELECT * FROM users', conn)")
    users_df = pd.read_sql_query("SELECT * FROM users", conn)
    print("All Users:")
    print(users_df)
    print()

    # Query 2: Select all orders
    print(">>> pd.read_sql_query('SELECT * FROM orders', conn)")
    orders_df = pd.read_sql_query("SELECT * FROM orders", conn)
    print("All Orders:")
    print(orders_df)
    print()

    # Query 3: Join users and orders
    print(">>> pd.read_sql_query('SELECT orders.id AS order_id, users.name AS user_name, orders.product_name, orders.quantity, orders.price, orders.order_date FROM orders JOIN users ON orders.user_id = users.id', conn)")
    joined_df = pd.read_sql_query("""
        SELECT
            orders.id AS order_id,
            users.name AS user_name,
            orders.product_name,
            orders.quantity,
            orders.price,
            orders.order_date
        FROM orders
        JOIN users ON orders.user_id = users.id
    """, conn)
    print("Orders with User Information:")
    print(joined_df)

# Run the main function
if __name__ == "__main__":
    main()

# Close the connection
conn.close()