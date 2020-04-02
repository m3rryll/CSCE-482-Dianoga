# Generated by Django 3.0.4 on 2020-04-02 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to='img/'),
        ),
    ]
