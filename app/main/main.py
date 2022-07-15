from flask import Blueprint, request, render_template, redirect, jsonify
from functios import get_posts_all, get_post_by_pk, get_comments_by_post_id,\
    search_for_posts, get_posts_by_user, save_tag, save_bookmarks, remove_bookmarks, get_bookmarks


main_blueprint = Blueprint("main", __name__, static_folder='static', template_folder='templates')


@main_blueprint.route('/')
def main():
    posts = get_posts_all()

    return render_template('index.html', posts=posts)


@main_blueprint.route('/posts/<int:postid>')
def post(postid):
    posts = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    count_comments = len(comments)

    return render_template('post.html', post=posts, comments=comments, count_comments=count_comments)


@main_blueprint.route('/search/')
def search():

    return render_template('search.html')


@main_blueprint.route('/posts/')
def s_search():
    query = request.args['s']
    posts = search_for_posts(query)
    count_posts = len(posts)

    return render_template('search.html', query=query, posts=posts, count_posts=count_posts)


@main_blueprint.route('/users/<username>')
def users(username):
    save_tag()
    user_posts = get_posts_by_user(username)

    return render_template('user-feed.html', posts=user_posts)


@main_blueprint.route('/tag/<name_tag>')
def user_tag(name_tag):
    "я так и не смог реализовать данную вьюшку, подскажите что у меня здесь не провильно"
    posts = [x for x in get_posts_all() if name_tag in x["text_tag"]]

    return render_template('tag.html', posts=posts)


@main_blueprint.route('/bookmarks/')
def bookmarks():
    bookmarks = get_bookmarks()

    return render_template('bookmarks.html', bookmarks=bookmarks)



@main_blueprint.route('/bookmarks/add/<int:postid>')
def add_post(postid):
    save_bookmarks(postid)

    return redirect("/", code=302)


@main_blueprint.route('/bookmarks/remove/<int:postid>')
def remove_post(postid):
    remove_bookmarks(postid)

    return redirect("/", code=302)








