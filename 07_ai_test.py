import os
from google import genai

client = genai.Client()

print("--- Sending Request to Gemini API ---")

response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents='Hello Gemini! This is Atharv. I am building an AI Code Auditor.',
)

print("\n--- AI Response Received ---")
print(response.text)