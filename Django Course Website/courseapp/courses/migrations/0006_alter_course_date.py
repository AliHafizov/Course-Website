# Generated by Django 4.2.4 on 2023-08-31 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_category_alter_course_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
