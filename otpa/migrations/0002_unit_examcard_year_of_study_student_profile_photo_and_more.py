# Generated by Django 5.0.3 on 2024-03-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('otpa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='examcard',
            name='year_of_study',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='student',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='profile_photos/'),
        ),
        migrations.AddField(
            model_name='exam',
            name='exam_units',
            field=models.ManyToManyField(related_name='exams', to='otpa.unit'),
        ),
        migrations.AddField(
            model_name='examcard',
            name='units',
            field=models.ManyToManyField(to='otpa.unit'),
        ),
    ]
