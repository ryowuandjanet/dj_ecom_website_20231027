# Generated by Django 4.2.6 on 2023-10-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=50, unique=True)),
                ('discount', models.PositiveIntegerField(help_text='discount in percentage')),
                ('active', models.BooleanField(default=True)),
                ('activate_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
