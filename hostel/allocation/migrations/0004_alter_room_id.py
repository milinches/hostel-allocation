# Generated by Django 3.2.9 on 2022-02-17 22:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('allocation', '0003_alter_room_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
