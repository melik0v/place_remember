# Generated by Django 4.1.3 on 2022-12-06 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("memories", "0003_alter_memory_created"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Photo",
            new_name="Image",
        ),
    ]
