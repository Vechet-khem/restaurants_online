from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class tblvillages(models.Model):
    uniqid = models.CharField(max_length=50,null=True,unique=True)
    khmer = models.CharField(max_length=255,null=True)
    english = models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return str(self.khmer)

    class Meta:
        ordering = ['id']
        db_table = 'tblvillages'

class tblcommunce(models.Model):
    uniqid = models.CharField(max_length=50,null=True,unique=True)
    khmer = models.CharField(max_length=255,null=True)
    english = models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return str(self.khmer)

    class Meta:
        ordering = ['id']
        db_table = 'tblcommunce'
        
class tbldistrict(models.Model):
    uniqid = models.CharField(max_length=50,null=True,unique=True)
    khmer = models.CharField(max_length=255,null=True)
    english = models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return str(self.khmer)

    class Meta:
        ordering = ['id']
        db_table = 'tbldistrict'

class tblprovince(models.Model):
    uniqid = models.CharField(max_length=50,null=True,unique=True)
    khmer = models.CharField(max_length=255,null=True)
    english = models.CharField(max_length=255,null=True)

    def __str__(self) -> str:
        return str(self.khmer)

    class Meta:
        ordering = ['id']
        db_table = 'tblprovince'

class tblsupplyer(models.Model):
    first_name = models.CharField(max_length=200, null=True , blank=True)
    last_name = models.CharField(max_length=200, null=True , blank=True)
    email = models.EmailField(max_length=200, null=True , blank=True)
    mobile = models.CharField(max_length=200, null=True , blank=True)
    company_name = models.CharField(max_length=225, null=True , blank=True)
    province = models.ForeignKey(tblprovince, on_delete=models.SET_NULL, null=True,related_name='province',to_field='uniqid')
    district = models.ForeignKey(tbldistrict, on_delete=models.SET_NULL, null=True,related_name='district',to_field='uniqid')
    commune = models.ForeignKey(tblcommunce, on_delete=models.SET_NULL, null=True,related_name='commune',to_field='uniqid')
    village = models.ForeignKey(tblvillages, on_delete=models.SET_NULL, null=True,related_name='village',to_field='uniqid')
    image = models.ImageField(default='user.png', upload_to='supplyer',null=False,blank=True)
    inputer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name='inputer')
    input_date = models.DateTimeField(auto_now=True)

    def get_image_url(self):
        return settings.BASE_API_URL + self.image.url

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'tblsupplyer'

class tblcustomer(models.Model):
    first_name = models.CharField(max_length=200, null=False , blank=True)
    last_name = models.CharField(max_length=200, null=False , blank=True)
    email = models.EmailField(max_length=200, null=True , blank=True)
    mobile = models.CharField(max_length=200, null=False , blank=True)
    province = models.ForeignKey(tblprovince, on_delete=models.SET_NULL, null=True,related_name='province_cus',to_field='uniqid')
    district = models.ForeignKey(tbldistrict, on_delete=models.SET_NULL, null=True,related_name='district_cus',to_field='uniqid')
    commune = models.ForeignKey(tblcommunce, on_delete=models.SET_NULL, null=True,related_name='commune_cus',to_field='uniqid')
    village = models.ForeignKey(tblvillages, on_delete=models.SET_NULL, null=True,related_name='village_cus',to_field='uniqid')
    image = models.ImageField(default='user.png', upload_to='customer',null=False,blank=True)
    inputer = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True,related_name='inputer_cus')
    input_date = models.DateTimeField(auto_now=True)

    def get_image_url(self):
        return settings.BASE_API_URL + self.image.url

    def __str__(self) -> str:
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'tblcustomer'