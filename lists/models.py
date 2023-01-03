from django.db import models
from django.urls import reverse
class List(models.Model):
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