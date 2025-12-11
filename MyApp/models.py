from django.db import models

# Create your models here.
class AboutMe(models.Model):
    headline = models.CharField(max_length=200)
    subheadline = models.CharField(max_length=300, blank=True)
    short_description = models.TextField(blank=True)
    long_description = models.TextField(blank=True)

    profile_image = models.ImageField(upload_to = 'aboutme/', blank=True, null=True)
    cv_file = models.FileField(upload_to = 'cv/', blank=True, null =True)

    email = models.EmailField(blank=True, unique= True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=100, blank=True)


    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    website = models.URLField(blank=True)



    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "About me"

    class Meta:
        verbose_name = "About Me"
        verbose_name_plural = "About Me"
