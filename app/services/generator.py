import random
import json

with open("app/data/templates.json") as f:
    TEMPLATES = json.load(f)

PERSONS = ["Virat Kohli", "PM Modi", "Shah Rukh Khan"]
PLACES = ["India Gate", "Mumbai", "Parliament"]

def generate_news(category: str, sentiment: str):
    template = random.choice(TEMPLATES[category][sentiment])

    return template.format(
        person=random.choice(PERSONS),
        place=random.choice(PLACES)
    )
