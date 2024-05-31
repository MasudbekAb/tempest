# Generated by Django 4.2.7 on 2024-05-31 08:43

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'avi', 'mov', 'gif', 'webp', 'pdf', 'doc', 'docx', 'mpeg'])], verbose_name='File')),
                ('file_type', models.CharField(choices=[('image', 'Image'), ('video', 'Video'), ('document', 'document'), ('gif', 'Gif'), ('other', 'Other')], max_length=10, verbose_name='File Type')),
            ],
            options={
                'verbose_name': 'Media',
                'verbose_name_plural': 'Media',
            },
        ),
        migrations.CreateModel(
            name='Nums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creativity', models.IntegerField()),
                ('hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pluses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=200)),
                ('money', models.CharField(max_length=200)),
                ('delivery', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card', models.CharField(max_length=200)),
                ('money', models.CharField(max_length=200)),
                ('delivery', models.CharField(max_length=200)),
                ('warranty', models.CharField(max_length=200)),
                ('branded', models.CharField(max_length=200)),
                ('afoordable', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TeamInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profession', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=200)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_image', to='main.media')),
            ],
        ),
        migrations.CreateModel(
            name='Short_products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sh_product_image', to='main.media')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sh_price', to='goods.product')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sh_title', to='goods.product')),
            ],
        ),
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history', models.TextField()),
                ('mission', models.TextField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='about_image', to='main.media')),
            ],
        ),
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_desc', models.CharField(max_length=200)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_image', to='main.media')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_price', to='goods.product')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel_title', to='goods.product')),
            ],
        ),
    ]
