import streamlit as st
import os
import openai

# Set the API key
openai.api_key = os.getenv("OPENAI_API_KEY")
# Create input text box for user to enter a prompt
prompt = st.text_area("Enter a prompt for the AI to complete", "Write an essay about Elon Musk and his contributions to technology:")

def generate_article(description):
# Use the OpenAI API to generate an article
    response = openai.Completion.create(
      model="text-davinci-003", 
      prompt= prompt,
      temperature=0.6,
      max_tokens=4175, # the tokens are the max number of words. 
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    # Extract the article from the API response
    article = response["choices"][0]["text"]
    return article

article = generate_article(prompt)
print(article)

# # Generate an outline
# outline = generate_outline()

# Display the outline
st.write(article)


