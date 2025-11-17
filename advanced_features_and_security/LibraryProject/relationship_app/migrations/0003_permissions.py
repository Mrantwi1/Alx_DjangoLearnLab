# 0003_custom_permissions.py
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0002_userprofile'), # Assumes this was your last migration
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            permissions={
                ('can_add_book', 'Can add new book entries'),
                ('can_change_book', 'Can edit existing book entries'),
                ('can_delete_book', 'Can delete book entries'),
            }
        ),
    ]
