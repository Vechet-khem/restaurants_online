# Generated by Django 4.1.4 on 2023-01-11 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0008_alter_tblsupplyer_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblsupplyer',
            name='mobile',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]