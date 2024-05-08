from search import generate_embeddings, match_documents
import streamlit as st
from streamlit_chat import message
import json
from llm_rag import generate_llm


def generate_response(prompt):

    embeddings = generate_embeddings(prompt)
    results = match_documents(embeddings, 0.5, 1)

    print(type(results))
    results_text = ""
    for id, doc, score in results:
        results_text += " " + "".join(doc)

    print(results_text)
    llm_response = generate_llm(user_input, results_text)

    print("rag: " + json.dumps(results) + " llm: " + llm_response)
    return llm_response


# Initialize session state
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []

# Create the Streamlit app
st.title("LLM Chatbot")

# Get user input
user_input = st.text_input("You:", key="user_input")

if user_input:
    output = generate_response(user_input)

    print(type(str(output)))

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

    # print(st.session_state.generated)


# Display the chat history
if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"])):
        message(st.session_state["past"][i], is_user=True, key=str(i) + "_user")
        message(st.session_state["generated"][i], key=str(i))
