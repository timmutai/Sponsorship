# Generated by Django 4.0.1 on 2022-04-25 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_rename_applicationdate_applications_applicationdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='applications',
            old_name='SponsorId',
            new_name='sponsorId',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='SponsorshipStatus',
            new_name='sponsorshipStatus',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='ApplicationDate',
            new_name='spplicationDate',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='StaffApproval',
            new_name='staffApproval',
        ),
        migrations.RenameField(
            model_name='applications',
            old_name='StudentId',
            new_name='studentId',
        ),
    ]