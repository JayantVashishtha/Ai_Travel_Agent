import streamlit as st
import requests

st.set_page_config(page_title="AI Travel Assistant", page_icon="🌍", layout="centered")

st.markdown("<h2 style='text-align: center;'>🌍 AI Travel Assistant</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 18px;'>Ask me anything related to your hotel, travel, or itinerary.</p>", unsafe_allow_html=True)


query = st.text_input("💬 Type your question", placeholder="e.g., What are the check-in timings?")

if st.button("Ask") and query:
    with st.spinner("Asking the AI agent..."):
        try:
            res = requests.post("http://127.0.0.1:8000/webhook", json={"message": query}, timeout=10)
            if res.status_code == 200:
                reply = res.json().get("reply", {}).get("result", "No reply found.")
                st.success(reply)
            else:
                st.error("Something went wrong with the API.")
        except Exception as e:
            st.error(f"❌ Failed to connect to backend: {e}")

st.markdown("<br><hr><center>Made with ❤️ by Jayant | Powered by Together.ai + LangChain</center>", unsafe_allow_html=True)
