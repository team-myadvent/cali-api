# Generated by Django 5.1.4 on 2024-12-17 19:11

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("guest_book", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="guestbook",
            old_name="detail",
            new_name="content",
        ),
    ]
