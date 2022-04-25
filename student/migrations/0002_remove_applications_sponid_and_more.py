# Generated by Django 4.0.1 on 2022-04-22 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applications',
            name='sponId',
        ),
        migrations.RemoveField(
            model_name='applications',
            name='sponsorUserId',
        ),
        migrations.AddField(
            model_name='applications',
            name='sponsorId',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sponsor.sponsor'),
        ),
        migrations.AlterField(
            model_name='applications',
            name='studentId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
    ]
