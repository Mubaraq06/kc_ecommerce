# Generated by Django 5.0.4 on 2024-05-10 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]
