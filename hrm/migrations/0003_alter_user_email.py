# Generated by Django 4.1.3 on 2022-11-24 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0002_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
