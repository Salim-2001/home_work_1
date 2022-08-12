from flask import Flask
from utils import *

candidats = get_all()
list = []

app = Flask(__name__)
@app.route("/")
def output_list():
    result = "<pre>"
    for candidat in candidats:
        img = candidat['picture']
        result += f"<img src='({img})'>\n" \
                  f"Имя {candidat['name']}\n" \
                  f"Позиция {candidat['position']}\n" \
                  f"Скиллы {candidat['skills']}\n" \
                  f"\n"
    result += "</pre>"
    return result

@app.route("/skills/<skill>")
def output_by_skill(skill):
    return get_by_skill(skill)

@app.route("/candidate/<int:pk>")
def output_candidat(pk):
    return get_by_pk(pk)


app.run()

