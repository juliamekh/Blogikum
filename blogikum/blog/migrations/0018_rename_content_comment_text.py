# Generated by Django 3.2.16 on 2024-05-12 13:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_alter_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='content',
            new_name='text',
        ),
    ]
