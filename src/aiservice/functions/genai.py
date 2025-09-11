from google import genai

class GenAIClient:
    def __init__(self):
        self.client = genai.Client()
