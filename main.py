import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY is missing from the .env file.")
else:
    print("✅ API Key loaded successfully. Sending request to Gemini...")


client = genai.Client(api_key=api_key)

try:
    # 3. Use the NEW Interactions API and the recommended model
    interaction = client.interactions.create(
        model="gemini-3.8-flash",  # <-- CHANGED
        input="Explain the difference between a Python list and a tuple in exactly two sentences."  # <-- CHANGED
    )

    print("\n--- Gemini's Response ---")
    print(interaction.output_text)  # <-- CHANGED

except Exception as e:
    print(f"\n❌ An error occurred: {e}")

