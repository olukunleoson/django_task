from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.User


#@receiver(post_save, sender=User)
#def user_profile(sender, instance, created, **kwargs):
    #if created:
        #user_profile.objects.create(user=instance)
    #instance.user_profile.save()    

class Comment(models.Model):
    post = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default='timezone:now')
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text