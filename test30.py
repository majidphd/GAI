import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "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"

def generate_response(prompt):
    # Call the OpenAI API to generate a response based on the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the engine, e.g., text-davinci-003
        prompt=prompt,
        max_tokens=150  # Adjust the maximum number of tokens in the response
    )
    return response.choices[0].text.strip()

def main():
    st.title("Streamlit with Large Language Model")

    # Get user input
    user_input = st.text_input("Enter a prompt:")

    if st.button("Generate Response"):
        if user_input:
            # Generate response using the GPT-3.5 model
            response = generate_response(user_input)
            st.markdown(f"**Model Output:** {response}")

if __name__ == "__main__":
    main()
