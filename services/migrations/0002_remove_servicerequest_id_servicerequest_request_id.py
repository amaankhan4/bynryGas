# Generated by Django 5.0.2 on 2024-11-28 17:25

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicerequest',
            name='id',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='request_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
