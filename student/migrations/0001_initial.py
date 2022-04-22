# Generated by Django 4.0.1 on 2022-04-21 20:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sponsor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_Name', models.CharField(max_length=200)),
                ('last_Name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=100)),
                ('phone_No', models.IntegerField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('birth_certificate', models.FileField(upload_to='files')),
                ('national_id', models.FileField(upload_to='files')),
                ('school_name', models.CharField(max_length=200)),
                ('school_address', models.CharField(max_length=200)),
                ('academic_level', models.CharField(max_length=100)),
                ('year_of_completion', models.DateField(null=True)),
                ('reason_for_application', models.TextField()),
                ('recomendation', models.FileField(upload_to='recomendation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='applications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsorUserId', models.IntegerField()),
                ('applicationDate', models.DateField(auto_now_add=True)),
                ('staffApproval', models.TextField(default='Pending review', max_length=20)),
                ('sponsorshipStatus', models.TextField(default='', max_length=20)),
                ('sponId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sponsor.sponsor')),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
