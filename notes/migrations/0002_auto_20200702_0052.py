# Generated by Django 3.0.8 on 2020-07-01 19:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notes',
            name='image',
        ),
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
