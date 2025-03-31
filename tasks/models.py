from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)  # Admin, User, Manager, etc.

    class Meta:
        db_table = "Role"

    def __str__(self):
        return self.name

class UserManager(BaseUserManager):
    def create_user(self, email, password=None,role=None,  **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        if not role:
            role = Role.objects.get_or_create(name="User")[0]
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # Hash password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        admin_role, _ = Role.objects.get_or_create(name="SuperAdmin")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_admin", True)
        return self.create_user(email, password,role=admin_role, **extra_fields)

class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False) 
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null=True)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        db_table = "User"

    def __str__(self):
        return self.email
    

class Task(models.Model):
    title = models.CharField(max_length=150,default="")
    description =models.CharField(max_length=150,default="")
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='tasks')
    
    class Meta:
        db_table="Task"
    
    def __str__(self):
        return self.title
    
