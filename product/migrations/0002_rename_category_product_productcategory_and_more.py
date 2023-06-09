# Generated by Django 4.1.8 on 2023-05-11 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category',
            new_name='productCategory',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='description',
            new_name='productDescr',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.AddField(
            model_name='product',
            name='productPriceBase',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='productdiscount',
            field=models.DecimalField(decimal_places=2, default='0', max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='productimage',
            field=models.CharField(default='url', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='productName',
            field=models.CharField(max_length=200),
        ),
    ]
