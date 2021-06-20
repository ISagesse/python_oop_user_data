from user import User
from post import Post

app_user_one = User("nn@nn.com", "Israel Sagesse", "pwd", "Web Developer")
app_user_one.get_user_info()

new_post = Post("Is the most skill developer", app_user_one.name)
new_post.get_post_info()