from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)


class Ad(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    company_name = models.CharField(max_length=200)
    company_url = models.URLField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    apply_email = models.EmailField()
    geographic_area = models.CharField(max_length=200, null=True,
                                       blank=True)

    tags = models.ManyToManyField(Tag, related_name="ads")
