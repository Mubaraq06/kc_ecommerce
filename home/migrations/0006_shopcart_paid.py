# Generated by Django 5.0.4 on 2024-04-29 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_shopcart'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
