from flask import Blueprint, render_template, request, send_from_directory, abort

from functions import add_to_json
from logger import logger

loader = Blueprint('loader', __name__)
POST_PATH = "posts.json"


@loader.route("/post", methods=["GET"])
def page_post_form():
    #добавляем пост
    return render_template("post_form.html")


@loader.route("/post", methods=["POST"])
def page_post_upload():
    #страница с добавленным постом
    picture = request.files.get('picture')
    content = request.form.get('content')
    filename = picture.filename
    picture.save(f"./uploads/{filename}")
    try:
        if not picture:
            raise ValueError("Ошибка загрузки: изображение не задано")
        if not content:
            raise ValueError("Ошибка загрузки: текст поста не задан")
        if picture.content_type not in ["image/jpeg", "image/png"]:
            raise TypeError("Загруженный файл - не картинка")
    except ValueError as e:
        logger.exception(e)
        return str(e)
    except TypeError as e:
        logger.exception(e)
        return str(e)
    try:
        new_post = add_to_json(POST_PATH, filename, content)
    except Exception as e:
        logger.exception(e)
        abort(500)
    return render_template("post_uploaded.html", post=new_post)


@loader.route("/upload/<path:path>")
def static_dir(path):
    #находим место картинки
    return send_from_directory("uploads", path)
