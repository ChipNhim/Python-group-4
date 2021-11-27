from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

class Room(models.Model):
    code = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    ROOM_TYPE = [(0, 'work'),(1, 'meeting')]
    room_type = models.SmallIntegerField(choices=ROOM_TYPE, null = True)

class Workcalendar(models.Model):
    work_date = models.DateField()
    work_time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)
    descript = models.TextField()
    pic = models.CharField(max_length=50)
    service = models.CharField(max_length=50)
    member = models.TextField()
    assign = models.CharField(max_length=50)

class Vehicle(models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    descript = models.TextField()
    team_leader = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)
    member = models.TextField()
    num_mem = models.SmallIntegerField()
    loc_start = models.CharField(max_length=50)
    loc_end = models.CharField(max_length=50)
    distance = models.CharField(max_length=10)
    VE_TYPE = [(0, 'zace'),(1, 'taxi')]
    ve_type = models.SmallIntegerField(choices=VE_TYPE, null = True)
    PLAN = [(0, 'Ke hoach'),(1, 'Dot xuat')]
    plan = models.SmallIntegerField(choices=PLAN, null = True)
    CHECK = [(0, 'Chua duyet'),(1, 'Da duyet')]
    check = models.SmallIntegerField(choices=CHECK, null = True)

class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    ROLES = [(0, 'Admin'),(1, 'Manager'),(2, 'Staff')]
    role = models.SmallIntegerField(choices=ROLES, null = True)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin