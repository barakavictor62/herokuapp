from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#User.profile = property(lambda u: Profile.objects.get_or_create(user=u)[0])

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture', blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class ContentWriting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    keywords = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    word_count = models.IntegerField()
    article_cost = models.CharField(max_length=20)
    date_posted = models.DateTimeField(auto_now_add=True)
    is_done = models.IntegerField(default=0)

class WebsiteBuilding(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    navigation_contents = models.CharField(max_length=500)
    website_cost = models.CharField(max_length=20)
    additional_instructions = models.CharField(max_length=1000)
