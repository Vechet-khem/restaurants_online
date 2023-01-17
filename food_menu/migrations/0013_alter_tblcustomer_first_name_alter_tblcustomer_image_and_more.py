# Generated by Django 4.1.4 on 2023-01-17 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0012_tblcustomer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblcustomer',
            name='first_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tblcustomer',
            name='image',
            field=models.ImageField(blank=True, default='user.png', upload_to='customer'),
        ),
        migrations.AlterField(
            model_name='tblcustomer',
            name='last_name',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='tblcustomer',
            name='mobile',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
