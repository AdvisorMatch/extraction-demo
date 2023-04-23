from django.db import models


# There is no keywords in the database yet.


class Advisor(models.Model):
    full_name = models.CharField(max_length=500)

    def __str__(self):
        return self.full_name


class Work(models.Model):
    title = models.CharField(max_length=500)  # English title
    abstract = models.TextField()  # English abstract
    year = models.IntegerField()  # Project year
    # ID from source - Keep Django and source independent
    source_id = models.IntegerField()
    # In this demo, the work is either project or thesis.
    # Should be enum on production
    work_type = models.CharField(max_length=500)  # Project, Thesis (from Projar), Research (by professor)
    advisor = models.ForeignKey(Advisor, on_delete=models.CASCADE)
    raw_keywords = models.CharField(max_length=500)  # Keywords from soruces

    def __str__(self):
        return f"{self.title} ({self.year})"
