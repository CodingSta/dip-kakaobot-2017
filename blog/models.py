from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    conent = models.TextField()
    author = models.CharField(max_length=20)
    status = models.CharField(
        max_length=1,
        choices=[
            ('d', 'Draft'),
            ('p', 'Published'),
            ('w', 'Withdrawn'),
        ],
        default='d'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.title
