# central/genai_client.py
import os
import requests
import json

# อ่านจาก environment หรือตั้งค่าใน config
GENAI_URL = os.environ.get("GENAI_URL", "https://genai.example/api/v1/consciousness")
GENAI_API_KEY = os.environ.get("GENAI_API_KEY", "")

def send_consciousness(payload: dict) -> dict:
    """
    ส่ง payload ไปยัง GENAI endpoint.
    payload จะถูกบรรจุภายใต้ field 'จิตรสำนึก' ตามที่คุณขอ
    """
    body = {
        "จิตรสำนึก": payload
    }
    headers = {
        "Content-Type": "application/json"
    }
    if GENAI_API_KEY:
        headers["Authorization"] = f"Bearer {GENAI_API_KEY}"

    try:
        resp = requests.post(GENAI_URL, headers=headers, data=json.dumps(body), timeout=10)
        resp.raise_for_status()
        return {"ok": True, "status_code": resp.status_code, "response": resp.json() if resp.text else None}
    except Exception as e:
        return {"ok": False, "error": str(e)}
