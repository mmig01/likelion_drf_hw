from django.db import models

# Create your models here.
class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, null=False , blank=False)
    content = models.TextField(max_length=200, null=False , blank=False)
    debut = models.TextField(null=False ,blank=False)

class Song(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False , blank=False)
    singer = models.ForeignKey(Singer, blank=False, null=False, on_delete=models.CASCADE, related_name='songs')
    content = models.TextField(max_length=200, null=False , blank=False)
    release = models.TextField(null=False , blank=False)
