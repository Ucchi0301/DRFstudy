from django.db import models
from django_boost.models.mixins import UUIDModelMixin
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        db_table = "post" 

class Group(UUIDModelMixin, models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "group" 
        
class GroupMembership(UUIDModelMixin, models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        db_table = "group_membership"