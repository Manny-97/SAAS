# Generated by Django 4.1.5 on 2023-01-08 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0002_alter_historicalstats_track"),
    ]

    operations = [
        migrations.AddField(
            model_name="notifygroup",
            name="notify",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="monitor.websites",
            ),
            preserve_default=False,
        ),
    ]
