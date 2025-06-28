import os
from dotenv import load_dotenv

def load_config():
    load_dotenv()
    config = {
        "SHODAN_API_KEY": os.getenv("SHODAN_API_KEY"),
        "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        # Add other configurations here
    }
    return config


