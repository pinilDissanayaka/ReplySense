import streamlit as st


st.set_page_config(page_title="ReplySense", page_icon=":robot_face:")


st.title('Email Reply Automation')


st.header("Welcome to Email Reply Automation!")

st.image("asset/banner.jpg")

st.write("This app helps you automatically generate email replies using GPT-4.")

### Key Features:
st.write("- **Unread Emails**: View the latest unread emails from your inbox.")
st.write("- **Automated Reply Generation**: Generate intelligent, context-aware replies using GPT-4.")
st.write("- **Reply Management**: Once a reply is generated, you can send it directly to the email sender.")

st.subheader("**How it Works**:")
st.write("1. The app fetches the latest unread emails.")
st.write("2. You can click to generate a reply for each email.")
st.write("3. Once the reply is generated, you can review it and send it.")

st.write("This app saves you time by automating responses to common inquiries and routine emails.")


