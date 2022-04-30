from flask import Blueprint, render_template, request, abort

from functions import search_parameter, load_posts, validate_JSON
from logger import logger

main = Blueprint('main', __name__)

POST_PATH = "posts.json"


@main.route('/')
def profile_page():
    return render_template("index.html")


@main.route("/list")
@main.route("/search")
def search_page():
    try:
        posts = load_posts(POST_PATH)
        validate_JSON(posts)
    except Exception as e:
        logger.exception(e)
        abort(500)
    s = request.args.get("s")
    if s:  # если в запросе есть параметр s, т.е. перешли по роуту '/search'
        chosen_posts = search_parameter(s)
        logger.info(f"Поиск по фразе: {s}")
        return render_template('post_list.html', posts=chosen_posts, s=s)
    # иначе перешли по '/list'
    return render_template('post_list.html', posts=posts)



