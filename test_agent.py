import requests

# 👇 Yaha tumhara NGROK URL ya localhost API URL daalna hai
url = "http://127.0.0.1:8000/webhook"   # ⬅️ VS Code ya PyCharm me run kar rahe ho toh ye use karo
# url = "https://xxxxxx.ngrok-free.app/webhook"  # ⬅️ Agar ngrok chal raha hai toh ye use karo

# 👇 Test input message
payload = {
    "message": "What are the check-in timings?"
}
print("📨 Sending POST request...")
try:
    res = requests.post(url, json=payload, timeout=10)
    print("✅ POST request sent.")
except Exception as e:
    print("❌ Failed to send request:", e)
    exit()
# 👇 Send POST request
# res = requests.post(url, json=payload)

# 👇 Output handling
print("Status Code:", res.status_code)
print("Raw Text Response:", res.text)

try:
    print("AI Agent Reply:", res.json())
except Exception as e:
    print("❌ Error parsing JSON:", e)
