from django.db import models


class QueryModel(models.Model):
    """ model for storing queries """
    query_date = models.DateTimeField(auto_now_add=True)
    query = models.CharField(max_length=1000)

    def __str__(self):
        return self.query[:15]
