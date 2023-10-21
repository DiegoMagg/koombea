from django.contrib.postgres.fields import ArrayField
from django.db import models


class PageContent(models.Model):
    SUCCESS = 'success'
    IN_PROGRESS = 'in progress'
    FAILURE = 'failure'
    STATUS_CHOICES = [
        (SUCCESS, 'Success'),
        (IN_PROGRESS, 'In progress'),
        (FAILURE, 'Failure'),
    ]
    user = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default='Page processing')
    url = models.URLField()
    links = ArrayField(ArrayField(models.CharField(max_length=255), size=2), null=True)
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default=IN_PROGRESS)

    def __str__(self):
        return self.name

    @property
    def total_links(self):
        return len(self.links) if self.links else 0

    class Meta:
        db_table = 'page_content'
        ordering = ['user', 'name']
