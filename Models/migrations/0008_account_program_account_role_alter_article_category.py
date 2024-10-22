# Generated by Django 4.2.15 on 2024-10-22 05:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Models", "0007_article_category_article_image_alter_article_title_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="program",
            field=models.CharField(
                blank=True,
                choices=[
                    ("ABCOM", "ABCOM"),
                    ("ABMMA", "ABMMA"),
                    ("AHM", "AHM"),
                    ("BACOMM", "BACOMM"),
                    ("BARNCII", "BARNCII"),
                    ("BEED", "BEED"),
                    ("BMMA", "BMMA"),
                    ("BPP NCII", "BPP NCII"),
                    ("BSA", "BSA"),
                    ("BSAIS", "BSAIS"),
                    ("BSAT", "BSAT"),
                    ("BSB", "BSB"),
                    ("BSBA", "BSBA"),
                    ("BSC", "BSC"),
                    ("BSCS", "BSCS"),
                    ("BSE", "BSE"),
                    ("BSED", "BSED"),
                    ("BSHM", "BSHM"),
                    ("BSHRM", "BSHRM"),
                    ("BSIT", "BSIT"),
                    ("BSIT(TEST)", "BSIT(TEST)"),
                    ("BSMLS", "BSMLS"),
                    ("BSMT", "BSMT"),
                    ("BSN", "BSN"),
                    ("BSN (YIBU)", "BSN (YIBU)"),
                    ("BSNED", "BSNED"),
                    ("BSOT", "BSOT"),
                    ("BSP", "BSP"),
                    ("BSPSY", "BSPSY"),
                    ("BSPT", "BSPT"),
                    ("BSPT (YIBU)", "BSPT (YIBU)"),
                    ("BSRT", "BSRT"),
                    ("BSRT (YIBU)", "BSRT (YIBU)"),
                    ("BSTM", "BSTM"),
                    ("BSTRM", "BSTRM"),
                    ("CCNCII", "CCNCII"),
                    ("CCPIII-TAFE", "CCPIII-TAFE"),
                    ("CGNCII", "CGNCII"),
                    ("CGNCII (T)", "CGNCII (T)"),
                    ("CHSNCII", "CHSNCII"),
                    ("CTP", "CTP"),
                    ("DB", "DB"),
                    ("DBM-KENT", "DBM-KENT"),
                    ("DM", "DM"),
                    ("DMM-KENT", "DMM-KENT"),
                    ("EIMNCII", "EIMNCII"),
                    ("FBSNCII", "FBSNCII"),
                    ("FL", "FL"),
                    ("HSKNCII", "HSKNCII"),
                    ("MAP", "MAP"),
                    ("MAP (YIBU)", "MAP (YIBU)"),
                    ("MBA", "MBA"),
                    ("MBA (YIBU)", "MBA (YIBU)"),
                    ("MD", "MD"),
                    ("MD(TEST)", "MD(TEST)"),
                    ("MISICT", "MISICT"),
                    ("MSN", "MSN"),
                    ("PNCIV", "PNCIV"),
                    ("PRE-DENT", "PRE-DENT"),
                    ("SMAWNCI", "SMAWNCI"),
                    ("SMAWNCII", "SMAWNCII"),
                    ("VACOMLIT", "VACOMLIT"),
                    ("WSA", "WSA"),
                ],
                default="BSIT",
                max_length=64,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="account",
            name="role",
            field=models.CharField(
                choices=[
                    ("Student", "Student"),
                    ("Program Chair", "Program Chair"),
                    ("Dean", "Dean"),
                ],
                default="Student",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.CharField(
                choices=[
                    ("Events", "Events"),
                    ("Announcements", "Announcements"),
                    ("Student Activities", "Student Activities"),
                    ("General", "General"),
                ],
                default="General",
                max_length=256,
            ),
        ),
    ]
