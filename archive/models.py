from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

CATEGORY_CHOICES = {
    ('Dj', 'Django'),
    ('R', 'Ruby')
}


class Post(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    custom_id = models.IntegerField()
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    publish_date = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    comments = models.ManyToManyField("Comment")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return self.title
