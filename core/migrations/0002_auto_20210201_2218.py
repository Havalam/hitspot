# Generated by Django 3.0.8 on 2021-02-01 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='_pwd',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
    ]
