from django.db import models
from django.contrib.auth.models import User

#MusicTalk
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    image = models.ImageField(upload_to='image/', default='')

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

#댓글
class Comment(models.Model):
    comment = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    #models.ForeignKey : 어떤 게시물의 댓글인지 참조
    #on_delete=CASCADE : 게시물이 삭제되면 댓글도 삭제

    def __str__(self):
        return self.comment #comment을 보여줌


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

