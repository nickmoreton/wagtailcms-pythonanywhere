# Generated by Django 4.1.3 on 2022-12-01 17:58

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_blogcategory"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpage",
            name="categories",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, to="blog.blogcategory"
            ),
        ),
    ]
