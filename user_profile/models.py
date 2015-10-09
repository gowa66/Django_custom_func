from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	bio = models.TextField(max_length=500, null=True, blank=True)


	def __unicode__(self):
		return self.user.username

from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
	if created:
		profile, new = UserProfile.objects.get_or_create(user=instance)