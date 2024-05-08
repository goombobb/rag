from pgvector.psycopg2 import register_vector
import psycopg2
import numpy as np
from pg import get_database_connection
from embed import generate_embeddings


def match_documents(query_embedding, match_threshold, match_count):
    # Establish a connection to the PostgreSQL database
    conn = get_database_connection()
    cur = conn.cursor()

    # Register the vector type with psycopg2
    register_vector(conn)

    cur.execute(
        """
        SELECT id, document, embedding <=> %s AS similarity
        FROM items
        ORDER BY similarity
        LIMIT %s
    """,
        (query_embedding, match_count),
    )
    # conn.close()

    return cur.fetchall()


def run():

    # Define a function to perform a cosine similarity search

    # Generate an example embedding to search for
    example_text = "how to handle a 455 http response?"
    example_text1 = "what to do when i can't access customer connect site?"
    example_embedding = generate_embeddings(example_text)

    # Perform the search and print the results
    results = match_documents(example_embedding, 0.5, 1)
    for id, content, similarity in results:
        print(f"ID: {id}, Content: {content}, Similarity: {similarity}")


if __name__ == "__main__":
    run()
