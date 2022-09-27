from django.db import models

# Create your models here.
POST_TYPE_CHOICES = (
    (1, 'Animals'),
    (2, 'Cars'),
    (3, 'Recipes'),
    (4, 'Nature'),
    (5, 'Other'),
)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True, blank=True, null=True)
    stars = models.IntegerField(null=True)
    type = models.IntegerField(null=True ,choices=POST_TYPE_CHOICES)



coment_type_choices = (
    (1, 'Aggresive'),
    (2, 'Kind'),
    (3, 'Other'),
    (4, 'IDK')
)

class Comment(models.Model):
    from_name = models.CharField(max_length=20)
    to_name = models.CharField(max_length=20)
    message = models.TextField(null=False)
    time = models.DateField(auto_now_add=True, blank=False, null=False)
    type_message = models.IntegerField(choices=coment_type_choices, null=True)