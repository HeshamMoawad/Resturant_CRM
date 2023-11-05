from django.db import models
from django.contrib.auth.models import AbstractUser 
# Create your models here.
class Agent (AbstractUser):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.username}"
    
    class Meta:
        verbose_name = 'Agent'
        verbose_name_plural = "Agents"



class Branch(AbstractUser):
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.username}"
    
    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = "Branches"



# Define the related_name for groups and user_permissions
Agent.groups.field.remote_field.related_name = 'agent_groups'
Agent.user_permissions.field.remote_field.related_name = 'agent_user_permissions'
Branch.groups.field.remote_field.related_name = 'branch_groups'
Branch.user_permissions.field.remote_field.related_name = 'branch_user_permissions'
