from pathlib import Path
import hashlib
import google.generativeai as genai
import PyPDF2


TEXT_API_KEY = 'AIzaSyAvw5v7lTEkG06xwNTNG69outIzHKV4yO0'

genai.configure(api_key=TEXT_API_KEY)
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }
    #Safety Measures for AI
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    ]

# Initialize the model for text generation
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    safety_settings=safety_settings,
    generation_config=generation_config,
    )

pathname = "./Nadeem Mohammed.pdf"
def extract_pages(pathname: str) -> list[str]:
    parts = [f"--- START OF PDF ${pathname} ---", f"--- END OF PDF ${pathname} ---"]
    pdf_reader = PyPDF2.PdfReader(pathname)
    for page_num in range(len(pdf_reader.pages)):
      page = pdf_reader.pages[page_num]
      text = page.extract_text()  # Extract text from the page
      parts.append(f"--- PAGE {page_num} ---")
      parts.append(text)
      prompt = "Whats in this PDF?"
      user_input = parts + [prompt] 
    return user_input

convo = model.start_chat(history=[
   {
      "role": "user",
      "parts": extract_pages(pathname) 
   }
])

# Option 1: Wait a short time (adjust delay as needed)
import time
time.sleep(2)  # Wait for 2 seconds

print(convo.last)