from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(email=email, **extra_fields)

        user.set_password(password)

        if email == "rafaproyectosfuturos@gmail.com":
            user.is_staff = True
            user.is_superuser = True
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        superuser = self.create_user(email, password, **extra_fields)

        superuser.is_superuser = True
        superuser.is_staff = True
        superuser.save()
        return superuser
    

class UserAccount(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(blank = False, null = False, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

