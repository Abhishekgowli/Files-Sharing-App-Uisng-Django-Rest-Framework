# Generated by Django 3.2.7 on 2022-02-12 03:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='folder',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('878392d8-5303-407a-838b-c0cd15da4e6d'), editable=False, primary_key=True, serialize=False),
        ),
    ]