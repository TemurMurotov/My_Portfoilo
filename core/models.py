from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    tech_stack = models.CharField(max_length=300, help_text="Vergul bilan ajrating: Django, Python, PostgreSQL")
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order', '-created_at']

    def __str__(self):
        return self.title



class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.platform


