# Generated by Django 5.1.3 on 2024-11-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_alter_payment_options_alter_paymentmethod_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymentmethod',
            name='external_id',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='ID externo mercadopago'),
        ),
    ]
