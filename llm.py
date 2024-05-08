import requests
import json

# Define the API endpoint and request body
url = "http://localhost:11434/api/generate"
request_body = {"model": "llama2", "prompt": "Why is the sky blue?"}

# Convert the request body to JSON
json_data = json.dumps(request_body)

# Set the headers
headers = {"Content-Type": "application/json"}

# Make the POST request
response = requests.post(url, data=json_data, headers=headers)

answer = ""
for line in response.iter_lines():
    if line:
        # Process the line of data
        # print(line)
        answer += json.loads(line.decode())["response"]
print(answer)

# # Check the response status code
# if response.status_code == 200:
#     # Print the response content
#     print(response.content)
# else:
#     # Print the error message
#     print(f"Error: {response.status_code} - {response.text}")


# # response = requests.get(api_url, headers=headers, stream=True)

# # for line in response.iter_lines():
# #     if line:
# #         # Process the line of data
# #         print(line)
