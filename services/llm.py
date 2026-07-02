import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def analyze_symptoms(patient):

    prompt = f"""
You are an AI Medical Educational Assistant.

Patient Details:

Name: {patient['name']}
Age: {patient['age']}
Gender: {patient['gender']}
Height: {patient['height']} cm
Weight: {patient['weight']} kg
Symptoms: {patient['symptoms']}
Duration: {patient['duration']}
Temperature: {patient['temperature']} °C

Provide the output in this exact format.

🩺 Possible Conditions
• 2-5 possible conditions

📌 Reasons
• 2-5 short points

🏠 Home Care
• 2-5 points

⚠ Warning Signs
• 2-5 points

👨‍⚕ Recommended Doctor
• One doctor only

📢 Disclaimer
• One short sentence.

Rules:
- Keep the response under 250 words.
- Use only bullet points.
- No long paragraphs.
- Never say the patient definitely has a disease.
"""

    completion = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.4,
        max_tokens=600
    )

    return completion.choices[0].message.content