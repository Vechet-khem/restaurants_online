from django.db import models
from django.contrib.auth.models import User


class tblvillages(models.Model):
    uniqid = models.CharField(max_length=50,null=True)
    khmer = models.CharField(max_length=255,null=True)
    english = models.CharField(max_length=255,null=True)

    class Meta:
        ordering = ['id']
        db_table = 'tblvillages'

class tblcommunce(models.Model):
    uniqid = models.CharField(max_length=50,null=True)
    khmer = models.CharField(max_length=255,null=True)
    english = models.CharField(max_length=255,null=True)

    class Meta:
        ordering = ['id']
        db_table = 'tblcommunce'
        
class tbldistrict(models.Model):
    uniqid = models.CharField(max_length=50,null=True)
    khmer = models.CharField(max_length=255,null=True)
    english = models.CharField(max_length=255,null=True)

    class Meta:
        ordering = ['id']
        db_table = 'tbldistrict'

class tblprovince(models.Model):
    uniqid = models.CharField(max_length=50,null=True)
    khmer = models.CharField(max_length=255,null=True)
    english = models.CharField(max_length=255,null=True)

    class Meta:
        ordering = ['id']
        db_table = 'tblprovince'

class tblcustomer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile = models.CharField(max_length=200)
    village = models.ForeignKey(
        tblvillages,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='village'
    )
    district = models.ForeignKey(
        tbldistrict,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='district'
    )
    communce = models.ForeignKey(
        tblcommunce,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='communce'
    )
    province = models.ForeignKey(
        tblprovince,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='province'
    )
    image = models.ImageField(
        default='customer/dfcustomer.jpg',
        upload_to='customer'
    )
    create_date = models.DateTimeField(auto_now=True)
    inputer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['-create_date']
        db_table = 'tblcustomer'