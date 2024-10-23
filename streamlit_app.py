import streamlit as st
st.set_page_config(        page_title="My Page Title",)
st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
with st.sidebar:
    st.page_link("pages/p2.py", label="Page 2" , icon="🧪")
    st.page_link("pages/p1.py", label="Page 3", icon="🌎")