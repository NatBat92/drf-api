# Generated by Django 3.2.20 on 2023-07-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0006_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../gw2_logo_f1jkjh', upload_to='images/'),
        ),
    ]
