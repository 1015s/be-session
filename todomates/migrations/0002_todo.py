# Generated by Django 4.0.2 on 2022-07-13 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todomates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, max_length=20, null=True)),
                ('thumb_nail', models.ImageField(blank=True, null=True, upload_to='todo/')),
                ('is_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('pup_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='todomates.category')),
            ],
        ),
    ]
