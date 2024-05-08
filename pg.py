import numpy as np
import psycopg2
from psycopg2 import sql


def get_database_connection():

    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="master",
        )
        return conn
    except Exception as e:
        print("An error occurred while establishing the database connection:", e)
        return None


def insert(data=None):

    # Connect to the PostgreSQL database
    # conn = psycopg2.connect(
    #     host="localhost",
    #     port="5432",
    #     database="postgres",
    #     user="postgres",
    #     password="master",
    # )
    conn = get_database_connection()
    cur = conn.cursor()
    try:
        # Prepare SQL query to insert data
        query = "INSERT INTO items (document, embedding) VALUES (%s, %s);"

        # Insert each embedding
        for x in data:
            print("aaa")
            cur.execute(
                query,
                (
                    x["document"],
                    x["embedding"].tolist(),
                ),
            )  # Convert numpy array to list

        # Commit the transactions
        conn.commit()
        print("Embeddings inserted successfully.")

    except Exception as e:
        print("An error occurred:", e)
        conn.rollback()
    finally:
        cur.close()
        conn.close()

    # Example vector data
    # vector_data = [1, 2, 3, 4, 5]

    # print(data)
    # vector_data_np = np.array([1, 2, 3, 4, 5])
    # vector_data = vector_data_np.tolist()  # Convert to list

    # SQL query to insert data
    # query = "INSERT INTO items (embedding) VALUES (%s);"

    # cur.execute(query, (data.tolist()))
    # conn.commit()

    # cur.close()
    # conn.close()


def read():
    conn = get_database_connection()
    if conn is None:
        return
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM items;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    finally:
        cur.close()
        conn.close()


# read()
# vector_data_np = np.random.rand(2, 3)  # Example: 10 embeddings of 300 dimensions each
# vector_data = vector_data_np.tolist()

# insert(vector_data_np)

# read()
