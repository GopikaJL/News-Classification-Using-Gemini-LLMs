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
model = genai.GenerativeModel('models/gemini-1.5-flash-8b')
response = model.generate_content("What is python?")
Markdown(response.text)
Python is a high-level, general-purpose programming language.  This means:

* **High-level:**  It's designed to be relatively easy for humans to read and write, abstracting away many of the low-level details of computer hardware and memory management.  You don't need to worry as much about things like memory allocation as you would in lower-level languages like C or Assembly.

* **General-purpose:** It can be used for a wide variety of tasks, including:
    * **Web development:** Building websites and web applications (using frameworks like Django and Flask).
    * **Data science and machine learning:** Analyzing data, building predictive models, and creating visualizations (using libraries like NumPy, Pandas, Scikit-learn, and TensorFlow).
    * **Scripting and automation:** Automating repetitive tasks, such as managing files or interacting with other software.
    * **Desktop applications:** Creating graphical user interfaces (GUIs) for desktop applications (using libraries like Tkinter or PyQt).
    * **Game development:** Creating games (using libraries like Pygame).
    * **Embedded systems:**  Programming smaller devices like microcontrollers (though other languages are often favored here).

Python's popularity stems from its readability, extensive libraries, and large and active community. Its relatively gentle learning curve makes it a popular choice for beginners, while its powerful capabilities make it suitable for experienced programmers as well.  The core philosophy emphasizes code readability with the use of significant indentation.
