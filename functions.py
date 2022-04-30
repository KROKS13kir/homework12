import json
import re


def load_posts(path):
    # подгружаем json
    with open(path, "r", encoding="utf-8") as search_file:
        posts_mas = json.load(search_file)
    return posts_mas

def search_parameter(key_word):
    #поиск по ключевому слову
    posts_mas = load_posts("posts.json")
    result_posts = []
    for post in posts_mas:
        if re.search(r'\b' + key_word.lower() + r'\b', post['content'].lower()):
            result_posts.append(post)
    return result_posts


def validate_JSON(posts):
    #Считан ли список постов из файла
    if not isinstance(posts, list):
        raise ValueError("Загруженные данные не являются списком.")


def add_to_json(path, filename, cont):
    #добавляет запись в json
    fragment = {'pic': "uploads/" + filename, 'content': cont}
    posts = load_posts("posts.json")
    posts.append(fragment)
    with open(path, "w", encoding='utf-8') as add_post_file:
        json.dump(posts, add_post_file, ensure_ascii=False, indent=2)
    return {'pic': filename, 'content': cont}
