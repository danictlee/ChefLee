import streamlit as st
import requests

st.set_page_config(page_title="Chef Lee's Kitchen", page_icon="🍜")
st.title("🍜 Chef Lee's Digital Kitchen")
st.subheader("Ask me about Asian recipes!")

query = st.text_input("What are you craving? (e.g., 'I have shrimp and eggs')")

if st.button("Ask the Chef 👨‍🍳"):
    if query:
        with st.spinner("The Chef is reading the cookbook..."):
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/ask", 
                    json={"query": query}
                )
                
                if response.status_code == 200:
                    answer = response.json().get("answer")
                    st.success("Recipe Found!")
                    st.write(answer)
                else:
                    st.error(f"Chef is busy! Error: {response.status_code}")
            
            except Exception as e:
                st.error(f"Connection refused! Is the backend running? \n\nError: {e}")
    else:
        st.warning("Please enter a question first!")