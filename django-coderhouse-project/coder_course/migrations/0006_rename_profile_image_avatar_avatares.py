# Generated by Django 3.2.4 on 2022-06-21 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coder_course', '0005_rename_user_profile_avatar_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='profile_image',
            new_name='avatares',
        ),
    ]
