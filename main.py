from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)


@app.route('/')
def home():
    posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(posts_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)


@app.route('/post/<int:id>')
def read_blog(id):
    poster = Post(id)
    title_post = poster.post_title
    subtitle_post = poster.post_subtitle
    body_post = poster.post_content
    return render_template("post.html", title=title_post, subtitle=subtitle_post, content=body_post)


if __name__ == "__main__":
    app.run(debug=True)
