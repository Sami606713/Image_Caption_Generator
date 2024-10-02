import requests
from dotenv import load_dotenv
import os
load_dotenv()

def generate_caption(file):
    try:
        API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
        headers = {"Authorization": f"Bearer {os.getenv('hf_token')}"}
        data = file.read()
        response = requests.post(API_URL, headers=headers, data=data)
        return response.json()
    except Exception as e:
        return str(e)