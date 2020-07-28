from django.db import models
from cms.models.fields import PlaceholderField

class MsgDet(models.Model):
    title = models.CharField(max_length=255)
    short_text = PlaceholderField('content')
