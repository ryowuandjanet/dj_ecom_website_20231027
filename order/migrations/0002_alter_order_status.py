# Generated by Django 4.2.6 on 2023-10-30 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('On the way', 'On the way'), ('Recieved', 'Recieved'), ('Delivered', 'Delivered')], max_length=15),
        ),
    ]
