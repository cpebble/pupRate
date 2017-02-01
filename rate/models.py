from django.db import models

import os
def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

# Create your models here.
class Pupper(models.Model):
    name = models.CharField(max_length=20)
    age  = models.IntegerField()
    picture = models.ImageField(upload_to=get_image_path, blank=False, null=False)

    score = models.IntegerField(blank=False, default=1400)
