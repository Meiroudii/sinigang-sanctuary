from django.db import models

# TODO: User's relational db in reviews of foods, comments, ratings
# TODO: ^> User's class: Name, created_comment_dated, its_ratings_for_food_posts, comments
# TODO: User's comments db
# TODO: User's contact to the author fetching?
# TODO: Admin's account
# TODO: ^> Fethcing on db the blog posts
# TODO: Author's creating a blog, saving > db
# TODO: ^> Title, Heading, Subheading, date_created, paragraph
# TODO: ^> Including blog's photos, PROB: paragraph of format
# TODO: ^> posts on blogs with foods, add db ratings which relates(foregin key?) on users, get the average

class Post(models.Model):
  title = models.CharField(max_length=255)
  dish = models.CharField(max_length=255)
  description = models.CharField(max_length=60)
  content = models.TextField()
  publish_date = models.DateField(auto_now_add=True)  # Automatically sets date on creation

  def __str__(self):
      return f"{self.title}"
