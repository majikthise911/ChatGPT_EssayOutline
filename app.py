import streamlit as st
import os
import openai

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")
#openai.api_key = 
# Create input text box for user to enter a prompt
prompt = st.text_area("Enter a prompt for the AI to complete", "Create an outline for an essay about Nikola Tesla and his contributions to technology:")
# Define a function that generates an outline for an essay about Nikola Tesla
def generate_outline():
    # Use the OpenAI API to generate an outline
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=prompt,
      temperature=0.3,
      max_tokens=150,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    # Extract the outline from the API response
    outline = response["choices"][0]["text"]
    return outline

# Generate an outline
outline = generate_outline()

# Display the outline
st.write(outline)

