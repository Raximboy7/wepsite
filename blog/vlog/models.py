from django.db import models

# Create your models here.
class Post(models.Model):
    image = models.ImageField(upload_to='images',blank=True, null=True)
    title = models.CharField(max_length=200)
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(
         'auth.User',
         on_delete=models.CASCADE

    )



    def __str__(self):
        return self.title
