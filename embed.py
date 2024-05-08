from sentence_transformers import SentenceTransformer

# Load the Sentence Transformer model
model = SentenceTransformer("BAAI/bge-large-en-v1.5")


def generate_embeddings(text):
    return model.encode(text)
