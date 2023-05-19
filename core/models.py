from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser , BaseUserManager
from django.utils.translation import gettext_lazy as _








class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        if User.objects.filter(email=email).exists():
            raise ValueError('This email address is already in use.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)










class User(AbstractUser):
    username = None
    is_company = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
    def __str__(self):
        return f"{self.email}"


class Job(models.Model):
    author = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)    
    date = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return f"{self.author} - {self.title} - {self.date}"

