from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import Signal


class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, default='userName')
    userEmail = models.CharField(max_length=50, default='email..')
    userImg = models.ImageField(upload_to='userImages/')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Postmodel(models.Model):
    post_coise = (
        ('yahshi', "Yahshi"),
        ('yomon', "Yomon")
    )
    profile = models.ForeignKey(Profil, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    text = models.TextField()
    post_image = models.ImageField(upload_to='postImages/', blank=True, null=True)
    turi = models.CharField(max_length=20, choices=post_coise, default='Yahshi')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class ComentModel(models.Model):
    post_comment = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Postmodel, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey(Profil, on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self) -> str:
        return self.post_comment


def Create_profile(sender, instance, created, **kwargs):
    print(sender, instance, created)
    if created:
        Profil.objects.create(user=instance)
    else:
        profile = Profil.objects.get(user=instance)
        profile.userEmail = instance.email
        profile.name = instance.first_name
        profile.save()
    
Signal.connect(post_save, Create_profile, sender=User)