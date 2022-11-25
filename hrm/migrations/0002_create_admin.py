from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_admin(apps, schema_editor):
    user = apps.get_model('hrm', 'User')

    admin = user(
        email = 'admin@gmail.com',
        name = 'Admin',
        role = 'AD'
    )
    admin.password = make_password('1234', salt=None)
    admin.save()


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('hrm', '0001_initial')
    ]

    operations = [
        migrations.RunPython(create_admin, migrations.RunPython.noop),
    ]
