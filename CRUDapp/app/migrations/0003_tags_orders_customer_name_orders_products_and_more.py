# Generated by Django 4.1 on 2022-09-13 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_orders_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(choices=[('OutDoor', 'OutDoor'), ('InDoors', 'InDoors'), ('Appliances', 'Appliances'), ('Phones', 'Phones'), ('Electronics', 'Electronics'), ('Laptops', 'Laptops')], max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='customer_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.customer'),
        ),
        migrations.AddField(
            model_name='orders',
            name='products',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.products'),
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.tags'),
        ),
    ]
