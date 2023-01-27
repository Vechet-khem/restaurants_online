from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin
from django.conf import settings
from food_menu.models import *

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations: True

    def create_superuser(self, email, password, username,  **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True:
            return ValueError('Superuser must have is_staff True')
        if other_fields.get('is_superuser') is not True:
            return ValueError('Superuser must have is_superuser True')
        return self.create_user(email, password, username, **other_fields)

    def create_user(self, email, password, username, **other_fields):
        if not email:
            raise ValueError('You must to provide a valid email address!')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user

class User(AbstractBaseUser):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=200,unique=True)
    username = models.CharField(max_length=250, unique=True, null=False)
    # team = models.ForeignKey()
    contact = models.CharField(max_length=250)
    input_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='user.png', upload_to='user',null=False,blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    province = models.ForeignKey(tblprovince, on_delete=models.SET_NULL, null=True,related_name='province_us',to_field='uniqid')
    district = models.ForeignKey(tbldistrict, on_delete=models.SET_NULL, null=True,related_name='district_us',to_field='uniqid')
    commune = models.ForeignKey(tblcommunce, on_delete=models.SET_NULL, null=True,related_name='commune_us',to_field='uniqid')
    village = models.ForeignKey(tblvillages, on_delete=models.SET_NULL, null=True,related_name='village_us',to_field='uniqid')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def get_image_url(self):
        return settings.BASE_API_URL + self.image.url

    def _str_(self) -> str:
        return self.email

    class Meta:
        db_table = 'tbluser'