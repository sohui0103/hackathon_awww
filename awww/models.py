from django.db import models
from django.contrib.auth.models import User

#MusicTalk
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    # image = models.ImageField(upload_to='image/', default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    # 좋아요
    likes = models.ManyToManyField(User, related_name='blogpost_like')

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title



class Comment(models.Model):
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(
        Blog, null=True, blank=True, on_delete=models.CASCADE)
    #comment_writer = models.ForeignKey(Profile, on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.comment


# class Profile(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     website_url = models.URLField(blank=True)

#Play List
class Playlist(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    # image = models.ImageField(upload_to='image/', default='')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    # 좋아요
    mucislikes = models.ManyToManyField(User, related_name='musicpost_like')

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

