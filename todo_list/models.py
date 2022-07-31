from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    done = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tags")

    class Meta:
        ordering = ["done", "datetime"]

    def __str__(self):
        return self.content
