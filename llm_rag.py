import requests
import json


def generate_llm(query, rag_info):

    url = "http://localhost:11434/api/generate"
    headers = {
        "Content-Type": "application/json",
    }

    prompt_instructions = """
        You are an AI assistant that is tasked with answering a user's query. The user has provided a query. Your response should be generated based on the provided context, which provides question and answer format, and should be informative, relevant, and tailored to the user's needs.

        The user's query is: {query}

        The context information provided is:
        {context}

        Please generate a response that addresses the user's query, adhering strictly to the provided context information to inform and shape your response. Your response should be well-structured, coherent, and demonstrate your understanding of the context. do not add anything else beyond the solution provided in the context.  be less verbose.

        Remember to only use the information provided in the context, and do not make up or speculate about any additional details. Your goal is to provide a helpful and accurate response based on the available information.
        """

    # prompt = f"Query: {query}\nContext: {json.dumps(rag_info)}"

    prompt = prompt_instructions.format(query=query, context=rag_info)
    print("prompt", prompt)

    data = {
        "model": "llama2",
        "prompt": prompt,
        "options": {"temperature": 0.7, "top_p": 0.9, "top_k": 50},
        "rag_info": rag_info,
    }

    response = requests.post(url, headers=headers, json=data)

    answer = ""
    for line in response.iter_lines():
        if line:
            # Process the line of data
            # print(line)
            answer += json.loads(line.decode())["response"]

    print(answer)

    # try:
    #     response = json.loads(response.text)
    # except json.JSONDecodeError as e:
    #     print(f"JSON decoding error: {e}")
    #     print(f"Response text: {response.text}")
    #     return None
    # response_data = json.loads(response.text)

    return answer


# search rag


# Example usage
# prompt = "What is the capital of OliveLand?"
# rag_info = {
#     "retrieved_documents": [
#         {
#             "title": "Opie",
#             "content": "lala is the capital and most populous city of OliveLand.",
#         },
#         {
#             "title": "OliveLand",
#             "content": "OliveLand is a country located in Western Europe.",
#         },
#     ],
#     "retrieval_score": 0.1,
# }

# result = generate_llm(prompt, rag_info)
# print(result)
