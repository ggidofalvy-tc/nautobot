# Generated by Django 3.1.13 on 2021-07-02 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("extras", "0009_computedfield"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customfield",
            name="validation_maximum",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customfield",
            name="validation_minimum",
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
