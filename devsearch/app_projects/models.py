from django.db import models
import uuid


# Create your models here.
# A Django 'Model' can be considered as a table, and is built with Python classes inheriting from Django Models
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,  # Text fields are typically larger than CharField,
                                   blank=True)  # For Django, allowed to submit forms with this blank
    demo_link = models.CharField(max_length=2000,
                                 null=True,  # null means that values can be submitted to database when this is null
                                 blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag',  # As we define the Tag model further down in the script, quotes allow us to reference the model before setting it
                                  blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)  # Creates timestamp for us
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Review(models.Model):
    project = models.ForeignKey(Project, # Links Review model to Project model
                                on_delete=models.CASCADE)  # If Project is deleted, cascade change to reviews for that Project
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=(('up', 'Up Vote'),
                                                      ('down', 'Down Vote')))
    created = models.DateTimeField(auto_now_add=True)  # Creates timestamp for us
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)  # Creates timestamp for us
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
