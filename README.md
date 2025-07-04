# 🧳 AI Travel Agent with LangChain + Together.ai + Streamlit

This is an intelligent **AI-powered Travel Agent** app built using **LangChain**, **Together.ai (Mixtral)**, **FAISS**, and **Streamlit UI**, that answers travel-related queries in multiple languages based on custom FAQ data.

---

## 🚀 Features

- ✅ Natural Language Q&A based on custom travel FAQs
- 💾 FAISS-based vector store from CSV
- 🤖 LLM support via Together.ai (`Mixtral-8x7B-Instruct`)
- 🌐 FastAPI backend for structured API
- 📱 Classy Streamlit UI with input + response
- 🔗 Easy local or cloud deployment (Vercel, Streamlit Cloud)

---

## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/your-username/AI_Travel_Agent.git
cd AI_Travel_Agent

### 2. Create & Activate Virtual Environment

python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows

### 3. Install Dependencies

pip install -r requirements.txt
### 4. Add .env File
Create a .env file in root:

TOGETHER_API_KEY=your_together_api_key_here

### 🛠 Run Locally
### 🧠 Build Vector Store (from CSV)

python app/vectorstore.py

### 🔁 Run FastAPI Backend

uvicorn app.main:app --reload
FastAPI runs on http://127.0.0.1:8000

### 🧪 Test API

python test_agent.py

### 🎨 Run Streamlit UI

cd ui
streamlit run app.py
Make sure backend is running before starting UI.

### 🧠 To-Do / Future Improvements
 1. WhatsApp or Twilio Integration

 2. Image-based itinerary suggestions

 3. Admin dashboard to update FAQs

 4. Persistent user memory (Redis / DB)



### 📄 License
MIT License – free to use & modify


