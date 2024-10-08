# Generated by Django 5.1 on 2024-08-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_published_date_book_added_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(blank=True, null=True, upload_to='books/'),
        ),
        migrations.AddField(
            model_name='book',
            name='tag',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='added_date',
            field=models.DateTimeField(),
        ),
    ]
