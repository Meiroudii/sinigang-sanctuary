from django.db import models

# TODO: User's relational db in reviews of foods, comments, ratings
# TODO: ^> User's class: Name, created_comment_dated, its_ratings_for_food_posts, comments
# TODO: User's comments db
# TODO: User's contact to the author fetching?
class Users(models.Model):
    pub_date = models.DateTimeField("commented at")
    username = models.CharField(max_length=30)
    user_comments = models.CharField(max_length=300)
    like_count = models.IntegerField(default=0)
# TODO: Admin's account
# TODO: ^> Fethcing on db the blog posts
# TODO: Author's creating a blog, saving > db
# TODO: ^> Title, Heading, Subheading, date_created, paragraph
# TODO: ^> Including blog's photos, PROB: paragraph of format
# TODO: ^> posts on blogs with foods, add db ratings which relates(foregin key?) on users, get the average
