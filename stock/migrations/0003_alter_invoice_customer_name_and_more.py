# Generated by Django 4.0.5 on 2022-09-13 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='customer_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('hr', 'hr'), ('hr', 'hr'), ('hr', 'hr'), ('hr', 'hr'), ('hr', 'hr')], max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_total_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_one_unit_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_total_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='line_two_unit_price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='paid',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='phone_number',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total_price',
            field=models.FloatField(),
        ),
    ]