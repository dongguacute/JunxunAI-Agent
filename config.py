# config.py

OPENROUTER_API_KEY = "YOUR_API_KEY"
MODEL_NAME = "deepseek/deepseek-r1-0528:free"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "HTTP-Referer": "https://openrouter.ai/api/v1/",
    "X-Title": "Military Training Reflection",
    "Content-Type": "application/json"
}
