from django.db import models
from django.urls import reverse
from django.conf import settings

class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, on_delete=models.DO_NOTHING)
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text') # Ensures that an item's text is unique in a list
        
    def __str__(self):
        return self.text