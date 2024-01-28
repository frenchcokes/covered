import os
from dotenv import load_dotenv

load_dotenv()

skills = os.getenv("SKILLS")

print(skills)