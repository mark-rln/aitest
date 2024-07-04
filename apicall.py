import openai

# Set your OpenAI API key
api_key = 'your-api-key-here'

# Initialize the OpenAI client
openai.api_key = api_key

# Define the prompt for the model
prompt = "Write a poem about the beauty of nature."

# Call the OpenAI API
response = openai.ChatCompletion.create(
  model="gpt-4",  # specify the model you want to use
  messages=[
      {"role": "system", "content": "You are a helpful assistant."},
      {"role": "user", "content": prompt}
  ],
  max_tokens=150  # specify the maximum number of tokens in the response
)

# Print the response
print(response.choices[0].message['content'])
