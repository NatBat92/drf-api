# Generated by Django 3.2.20 on 2023-07-16 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='../gw2_logo_f1jkjh', upload_to='images/'),
        ),
    ]