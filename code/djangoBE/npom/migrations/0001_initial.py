# Generated by Django 4.2.19 on 2025-02-08 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=500, verbose_name='full name')),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('availability_starts_on', models.DateTimeField(verbose_name='availability start date')),
                ('availability_ends_on', models.DateTimeField(verbose_name='availability end date')),
            ],
        ),
        migrations.CreateModel(
            name='ProductRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=500)),
                ('quantity', models.IntegerField(default=1)),
                ('recived_on', models.DateTimeField(verbose_name='recived on')),
                ('expires_on', models.DateTimeField(verbose_name='expires on')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='npom.product')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=2500)),
                ('date', models.DateTimeField(verbose_name='event date')),
                ('location', models.CharField(max_length=500)),
                ('volunteers', models.ManyToManyField(related_name='events', to='npom.volunteer')),
            ],
        ),
    ]
