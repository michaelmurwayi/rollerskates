# Generated by Django 2.1.7 on 2019-02-20 04:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0002_import_example_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myobject',
            old_name='limit_quantity',
            new_name='quantity',
        ),
    ]
