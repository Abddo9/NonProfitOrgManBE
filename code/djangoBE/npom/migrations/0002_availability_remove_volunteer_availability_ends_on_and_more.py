# Generated by Django 4.2.19 on 2025-02-08 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('npom', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starts_on', models.DateTimeField(verbose_name='start on')),
                ('ends_on', models.DateTimeField(verbose_name='end on')),
            ],
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='availability_ends_on',
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='availability_starts_on',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='availabilities',
            field=models.ManyToManyField(related_name='volunteers', to='npom.availability'),
        ),
    ]
