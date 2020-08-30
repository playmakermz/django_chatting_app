from django.db import models

class pesan(models.Model):
    Pesan = models.CharField(max_length=100)
    detail = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
