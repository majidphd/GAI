from openai import OpenAI
import streamlit as st

with st.sidebar:
#    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    openai_api_key = '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'
    """
    ## :green[Generative AI]
    According to :red[(Andrew Ng)] Generative AI 
    able to do many of the things that a college 
    student following instructions might be able 
    to do. Some of its common use cases including 
    writing, reading, and chatting. For building 
    generative AI projects, we should includ the 
    life cycle of the project, with a variety of 
    technology options, such as prompting, retrieval 
    augmented generation, and fine tuning. Finally, 
    automation or augmentation could lead to new 
    workflows that don't just realize cost savings, 
    but lead to significant brand new value creation.
    """
    st.markdown("_____________________________")
    "[You can check out 704- Revision](https://704-revision.streamlit.app/)"
    "[And student predict streamlit](https://student-predict-parts.streamlit.app/)"
    "[Open GitHub to see codes](https://github.com/majidphd)"

st.title("💬 :blue[*Chatbot Generative AI*]")
st.markdown("🚀 ***A streamlit chatbot with OpenAI LLM: :orange[Done by MAJED ALZAHRANI]***")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you my friend?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    client = OpenAI(api_key=openai_api_key)
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
