# Generated by Django 3.0.6 on 2020-08-11 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messfeedback',
            name='feedback_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]