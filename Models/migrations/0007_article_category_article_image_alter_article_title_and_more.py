# Generated by Django 4.2.15 on 2024-10-22 03:01

import Models.utils.directory_helper
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Models", "0006_programhighlight_article_department_article_program"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="category",
            field=models.CharField(
                choices=[
                    ("News", "News"),
                    ("Events", "Events"),
                    ("Announcements", "Announcements"),
                    ("Student Activities", "Student Activities"),
                    ("General", "General"),
                ],
                default="General",
                max_length=256,
            ),
        ),
        migrations.AddField(
            model_name="article",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=Models.utils.directory_helper.get_article_media_directory,
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name="programhighlight",
            name="image",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to=Models.utils.directory_helper.get_program_highlight_directory,
            ),
        ),
    ]