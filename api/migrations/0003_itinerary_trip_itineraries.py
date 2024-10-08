# Generated by Django 5.1 on 2024-08-26 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_trip_date_alter_trip_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('priority', models.CharField(choices=[('H', 'High'), ('M', 'Medium'), ('L', 'Low')], default='H', max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='itineraries',
            field=models.ManyToManyField(to='api.itinerary'),
        ),
    ]
