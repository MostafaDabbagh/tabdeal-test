# Generated by Django 4.1.7 on 2023-03-05 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_rename_operation_accountrechargeorder_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountrechargeorder',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='saleorder',
            name='amount',
            field=models.PositiveIntegerField(),
        ),
    ]
