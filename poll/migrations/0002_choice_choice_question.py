# Generated by Django 3.1.1 on 2020-09-12 09:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='choice_question',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='poll.question'),
            preserve_default=False,
        ),
    ]
