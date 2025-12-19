from datetime import datetime

class Database:
    def __init__(self):
        self.posts = {}
        self.counter = 0

    def get_all_posts(self):
        return list(self.posts.values())

    def get_post_by_id(self, post_id: int):
        return self.posts.get(post_id)

    def create_post(self, post_data: dict):
        self.counter += 1
        post = {
            "id": self.counter,
            "title": post_data["title"],
            "content": post_data["content"],
            "author": post_data["author"],
            "published": post_data.get("published", False),
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.posts[self.counter] = post
        return post

    def update_post(self, post_id: int, post_data: dict):
        if post_id not in self.posts:
            return None
        existing_post = self.posts[post_id]
        for key, value in post_data.items():
            if value is not None:
                existing_post[key] = value
        return existing_post

    def delete_post(self, post_id: int):
        if post_id in self.posts:
            del self.posts[post_id]
            return True
        return False

db = Database()