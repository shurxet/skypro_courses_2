from flask import Blueprint, jsonify
from functios import get_posts_all, get_post_by_pk
import logging


logging.basicConfig(
        encoding='utf-8',
        level=logging.INFO,
        filename="logs/api.log",
        format='%(asctime)s [%(levelname)s] %(message)s')


api_blueprint = Blueprint("api", __name__)


@api_blueprint.route('/api/posts/')
def api_posts():
    data = get_posts_all()
    logging.info(f"запрос данных /api/posts/")
    return jsonify(data)


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post(post_id):
    data = get_post_by_pk(post_id)
    logging.info(f"запрос данных /api/posts/{post_id}")
    return jsonify(data)

