import streamlit as st
import json
import requests
import os
API_TOKEN = os.environ.get('API_TOKEN')


headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/sabre-code/pegasus-large-cnn-dailymail"


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))



st.set_page_config(layout='wide')
st.title("Text Summarisation App PEGASUS-large")
st.subheader('Input text below to be summarised', divider='rainbow')


# Create a text input widget
text_input = st.text_area(label="Input Text", height=200)
generated_summary = ""
# Define a function to generate the summary
def generate_summary(text):
    def query(payload):
        data = json.dumps(payload)
        response = requests.request("POST", API_URL, headers=headers, data=data)
        return json.loads(response.content.decode("utf-8"))
    
    data = query({"inputs": text})
    
    
    # Return the generated summary
    return data

# Add a button to trigger the generation of the summary
generate_button = st.button(label="Generate Summary")
if generate_button:
    # Call the generate_summary function when the button is clicked
    generated_summary = generate_summary(text_input)
    #st.success("Summary Generated!")


# Display the generated summary
st.markdown("## Summary")
st.success(generated_summary)