# Generated by Django 3.0.6 on 2020-06-15 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.CharField(choices=[('medical_tech', 'Medical Tech'), ('dental', 'Detal'), ('programming', 'Computer Programming'), ('security', 'Security'), ('database', 'Database'), ('project_management', 'Project Management')], max_length=32),
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
    ]
