# Generated by Django 4.2.4 on 2023-08-24 05:05

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Data_Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_saler', models.CharField(max_length=100)),
                ('name_buyer', models.CharField(max_length=100)),
                ('East_meter', models.FloatField()),
                ('West_meter', models.FloatField()),
                ('North_meter', models.FloatField()),
                ('South_meter', models.FloatField()),
                ('hypotenuse1', models.FloatField(blank=True, null=True)),
                ('hypotenuse2', models.FloatField(blank=True, null=True)),
                ('East', models.CharField(max_length=500)),
                ('West', models.CharField(max_length=500)),
                ('North', models.CharField(max_length=500)),
                ('South', models.CharField(max_length=500)),
                ('area', models.CharField(max_length=500)),
                ('price', models.FloatField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('subtitle_information_for_land', models.TextField(blank=True, max_length=5000, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='image_land')),
            ],
        ),
        migrations.CreateModel(
            name='Data_For_Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('happy_or_not', models.BooleanField()),
                ('created_at', models.DateField(default=django.utils.timezone.now)),
                ('defucalt', models.BooleanField()),
                ('notes_for_me', models.TextField(blank=True, max_length=5000, null=True)),
                ('who_with_me', models.CharField(blank=True, choices=[('Alone', 'Alone'), ('Abdelmonem', 'Abdelmonem'), ('Moahmed', 'Mohamed')], max_length=20, null=True)),
                ('were_this_land', models.CharField(blank=True, max_length=500, null=True)),
                ('Land', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='auter_land', to='app.data_land')),
            ],
        ),
    ]