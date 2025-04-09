# Generated by Django 5.2 on 2025-04-08 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
            options={
                'indexes': [models.Index(fields=['precio'], name='books_book_precio_4b17c3_idx')],
            },
        ),
    ]
