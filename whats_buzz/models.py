from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    post_type = models.CharField(max_length=2,
                                      choices=(
                                          ('FG', 'משחקי פייסבוק'),
                                          ('TY', 'בחן את עצמך'),
                                      ),
                                      default='FG')
    image_banner = models.ImageField(upload_to='%Y/%m/%d/', blank = True)
    buzz = models.BooleanField()
