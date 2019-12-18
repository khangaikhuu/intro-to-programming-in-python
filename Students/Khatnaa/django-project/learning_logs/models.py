from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)   # now date

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE) # topic ystval entry ystna
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

# class Meta:
#     verbose_name_plural = 'entries'
#     def __str__(self):
#         """Return a string representation of the model."""
#         return f"{self.text[:50]}..."


# python manage.py makemigrations learning_logs  ----djangod projectooo burtguulehed lg88050411