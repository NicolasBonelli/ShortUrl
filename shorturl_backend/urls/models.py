from djongo import models

class ShortURL(models.Model):
    original_url = models.URLField(max_length=500)
    short_code = models.CharField(max_length=6, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
