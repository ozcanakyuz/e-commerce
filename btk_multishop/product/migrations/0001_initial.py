# Generated by Django 4.2.7 on 2023-11-30 08:29

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('keywords', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayir')], max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('create_at', models.DateTimeField(auto_now=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='product.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
