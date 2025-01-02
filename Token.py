from kaggle_secrets import UserSecretsClient
from IPython.display import display
from IPython.display import Markdown
import os
import pathlib
import textwrap
user_secrets = UserSecretsClient()
apiKey = user_secrets.get_secret("GEMINI_API_KEY")
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
import google.generativeai as genai
genai.configure(api_key = apiKey)
