# Generated by Django 4.1.7 on 2023-03-05 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_game_create_by"),
    ]

    operations = [
        migrations.RenameField(
            model_name="game",
            old_name="create_by",
            new_name="created_by",
        ),
    ]
