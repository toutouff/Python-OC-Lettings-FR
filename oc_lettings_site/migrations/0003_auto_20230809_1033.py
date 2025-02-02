# Generated by Django 3.0 on 2023-08-09 10:33

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('oc_lettings_site', '0002_delete_profile'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            state_operations=[
                migrations.RemoveField(
                    model_name='letting',
                    name='address'
                ),
                migrations.DeleteModel(
                    name='Address',
                ),
                migrations.DeleteModel(
                    name='Letting',
                )],
            database_operations=[
                migrations.AlterModelTable(
                    name='Address',
                    table='lettings_address'
                ),
                migrations.AlterModelTable(
                    name='Letting',
                    table='lettings_letting'

                )
            ]
        )
    ]
