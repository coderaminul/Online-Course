# Generated by Django 4.0.3 on 2022-08-29 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userPanel', '0003_alter_blogs_blog_details_alter_comments_comm_detils_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='sl_image',
            field=models.FileField(upload_to=''),
        ),
    ]