from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """baseuser for creating user profiles"""

    def create_user(self, email, name, password=None):
        """creates a new user profile"""
        if not email:
            raise ValueError("User does not have an email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)
        
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def creat_super_user(self, email, name, password):
        """Create a new super user"""
        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """retrieve and return full name"""
        return self.name
    
    def short_name(self):
        """retrieve short name of user"""
        return self.name
    
    def __str__(self):
        """return string representation of user"""
        return self.email