import json
from blog.models import post


with open('posts.json') as f:
    posts_json = json.load(f)
for i in posts_json:
    posts = post(title=i['title'], author_id=i['user_id'], content=i['content'])
