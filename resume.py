import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

#.env
#OPENAIKEY=
#SKILLS=

f = open("test.txt", "r")


client = OpenAI(api_key=os.getenv("OPENAIKEY"))

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a cover letter maker, who makes cover letters tailored to a job."},
        {"role": "user", "content": "Write a cover letter which leverages these skills: " + os.getenv("SKILLS")}
    ]
)

print(completion.choices[0].message)