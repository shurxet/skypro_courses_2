import json
import re


posts = 'data/post.json'
comments = 'data/comments.json'
bookmarks = 'data/bookmarks.json'


def get_posts_all():
    with open(posts, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_comments():
    with open(comments, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def get_bookmarks():
    with open(bookmarks, 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data


def save_data(data, open_file):
    with open(open_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def get_posts_by_user(user_name):
    try:
        postes = [x for x in get_posts_all() if user_name.lower() in x['poster_name'].lower()]
    except ValueError:
        return "<h1> Такого пользователя нет или нет постов </h1>"
    else:
        return postes


def get_comments_by_post_id(pk):
    try:
        comment = [x for x in get_comments() if pk == x['post_id']]
    except ValueError:
        return "<h1> Такого поста нет или нет комментов </h1>"
    else:
        return comment


def search_for_posts(query):
    list_posts = [x for x in get_posts_all() if query.lower() in re.split(" |,|-|!|#|по", x['content'].lower())]

    return list_posts


def get_post_by_pk(pk):

    for post in get_posts_all():
        if pk == post['pk']:
            return post


def save_tag():
    load_posts = get_posts_all()

    for post in load_posts:
        post['text_tag'] = ""
        for i in re.split(" |,|-|!", post['content']):
            if '#' in i:
                post['text_tag'] += i

    save_data(load_posts, posts)



def test_api_list(data):
    message_text = ''

    if not type(data) == list:
        message_text += "это не список"
    else:
        message_text += "это список"
    return message_text


def save_bookmarks(post_id):
    load_posts = get_posts_all()
    load_bookmarks = get_bookmarks()

    for post in load_posts:
        if post_id == post["pk"]:
            load_bookmarks.append(post)

    save_data(load_bookmarks, bookmarks)


def remove_bookmarks(post_id):
    load_bookmarks = get_bookmarks()

    for book in load_bookmarks:
        if post_id == book["pk"]:
            load_bookmarks.remove(book)

    save_data(load_bookmarks, bookmarks)





















