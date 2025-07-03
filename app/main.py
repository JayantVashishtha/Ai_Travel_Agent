# from fastapi import FastAPI, Request
# from app.qa_chain import get_qa_chain
# import uvicorn
# import time
# app = FastAPI()
# qa_chain = get_qa_chain()
#
# @app.post("/webhook")
# async def webhook(request: Request):
#     print("✅ Received request")
#     start = time.time()
#     data = await request.json()
#     message = data.get("message", "")
#     if not message:
#         return {"error": "No message provided"}
#     try:
#         response = qa_chain.run(message)
#         print("🧠 LLM Response:", response)
#         return {"response": response}
#     except Exception as e:
#         print("❌ Error in qa_chain:", str(e))
#         return {"error": str(e)}
#
# def run():
#     uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
#
# if __name__ == "__main__":
#     run()


from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.qa_chain import get_qa_chain

app = FastAPI()

# ✅ Middleware sabse pehle configure kiya gaya tha
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],       # ✅ All domains allowed
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

qa_chain = get_qa_chain()

@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    print("📥 Incoming request data:", data)
    message = data.get("message", "")
    if not message:
        return {"error": "No message provided"}

    response = qa_chain.invoke({"query": message})
    return {"reply": response}
