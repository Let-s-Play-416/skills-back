from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,  PermissionsMixin)


class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if email is None:
            raise ValueError("User must have email")
        if username is None:
            raise ValueError("user must have username")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email,  password):
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
        


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username

