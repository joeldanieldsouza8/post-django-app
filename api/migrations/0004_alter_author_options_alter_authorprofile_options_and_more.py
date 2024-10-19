# Generated by Django 5.1.2 on 2024-10-19 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_authorprofile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['fullname'], 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='authorprofile',
            options={'verbose_name': 'Author Profile', 'verbose_name_plural': 'Author Profiles'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-importance_level'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
