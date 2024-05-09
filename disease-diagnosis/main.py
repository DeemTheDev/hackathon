import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('•', "*")
    return Markdown(textwrap.indent(text, '>', predicate=lambda _:True))

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

#Generate test from input 

model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is 2 + 2 ?")
to_markdown(response.text)