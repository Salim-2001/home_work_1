import json

def load_candidates(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = file.read()
        my_format = json.loads(data)
        return my_format


def get_all():
    return load_candidates("candidates.json")


def get_by_pk(pk):
    data = get_all()
    result = "<pre>"

    for candidat in data:
        url = candidat['picture']
        if pk == candidat["pk"]:
                result += f"<img src='({url})'>\n" \
                          f"Имя {candidat['name']}\n" \
                          f"Позиция {candidat['position']}\n" \
                          f"Скиллы {candidat['skills']}\n" \
                          f"\n"
    result += "</pre>"

    return result


def get_by_skill(skill_name):

    data = get_all()
    result = "<pre>"
    for candidat in data:
        if skill_name.lower() in candidat['skills']:
            result += f"Имя {candidat['name']}\n" \
                      f"Позиция {candidat['position']}\n" \
                      f"Скиллы {candidat['skills']}\n" \
                      f"\n"
    result += "</pre>"

    return result
