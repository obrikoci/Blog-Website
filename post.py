import requests

class Post:
    def __init__(self, id):
        self.post_title = ""
        self.post_subtitle = ""
        self.post_content = ""
        self.get_post(id)

    def get_post(self, id):
        posts_url = "https://api.npoint.io/c790b4d5cab58020d391"
        response = requests.get(posts_url)
        all_posts = response.json()
        for post in all_posts:
            if post["id"] == id:
                self.post_title = post["title"]
                self.post_subtitle = post["subtitle"]
                self.post_content = post["body"]

