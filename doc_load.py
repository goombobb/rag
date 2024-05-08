import csv
from sentence_transformers import SentenceTransformer
import os
from pg import insert, read

# Load the Sentence Transformer model
model = SentenceTransformer("BAAI/bge-large-en-v1.5")

# Open the CSV file
# Get the directory of the current script
current_dir = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(current_dir)

# Construct the path to the 'data' folder
# data_folder = os.path.join(dir_path, '..', 'data')
# os.path.dirname(os.path.realpath(__file__))
csv_file = os.path.join(parent_dir, "data/input.csv")
print(csv_file)
with open(csv_file, "r") as file:
    reader = csv.reader(file)

    # Skip the header row
    next(reader)

    # Iterate through the rows and create embeddings
    data = []
    for row in reader:
        text = row[0] + "," + row[1]

        print(text)
        # Create the embedding using the Sentence Transformer model
        embedding = model.encode(text)
        # print(embedding)
        # print(embedding.shape[0])
        # Append the embedding to the list
        data.append({"document": text, "embedding": embedding})
        # print(type(embedding))

    insert(data)
    # read()
    # Insert the embedding into the database

# Now you can use the embeddings for further processing or analysis
print(f"Created {len(embedding)} embeddings.")
