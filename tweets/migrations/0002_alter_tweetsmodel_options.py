# Generated by Django 4.2.2 on 2023-07-10 19:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweetsmodel',
            options={'ordering': ['-id']},
        ),
    ]
