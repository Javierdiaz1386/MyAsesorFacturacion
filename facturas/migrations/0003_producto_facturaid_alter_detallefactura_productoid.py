# Generated by Django 4.2.3 on 2023-07-17 03:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturas', '0002_inventario_remove_producto_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='facturaID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='facturas.factura'),
        ),
        migrations.AlterField(
            model_name='detallefactura',
            name='ProductoID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facturas.inventario'),
        ),
    ]
