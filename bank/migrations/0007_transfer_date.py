# Generated by Django 4.1.4 on 2022-12-19 20:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0006_alter_transfer_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]