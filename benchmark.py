import openai
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env
openai.api_key = os.getenv("OPENAI_API_KEY")
