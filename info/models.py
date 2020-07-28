from django.db import models
from cms.models.fields import PlaceholderField

class MsgDet(models.Model):
    """
    Detail
    """
    title = models.CharField(max_length=255)
    short_text = PlaceholderField('Description')
