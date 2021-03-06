# Generated by Django 3.2.6 on 2021-08-20 13:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treck',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('Name', models.CharField(max_length=100)),
                ('short_desc', models.CharField(max_length=1000)),
                ('long_desc', models.TextField()),
                ('days', models.CharField(blank=True, max_length=20, null=True)),
                ('distance', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('age', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('Price', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='treck-image')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='trekcategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('category_name', models.CharField(max_length=100)),
                ('category_desc', models.CharField(max_length=500)),
                ('cattegory_image', models.ImageField(upload_to='category-image')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Treck_Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('treckimage', models.ImageField(upload_to='trecks/treckname')),
                ('treckimg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.treck')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='treck',
            name='treckcat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.trekcategory'),
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('reviews', models.TextField()),
                ('review_number', models.IntegerField(blank=True, null=True)),
                ('treckreview', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.treck')),
                ('ureview', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Accounts.usersignup')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('Sitinerary', models.CharField(max_length=200)),
                ('treck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.treck')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Boodtreck',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('bookname', models.CharField(blank=True, max_length=100, null=True)),
                ('bookemail', models.CharField(max_length=254)),
                ('booknumber', models.CharField(max_length=13)),
                ('bookaddress', models.TextField()),
                ('booknotes', models.TextField(blank=True, null=True)),
                ('treckid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.treck')),
                ('userbookid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.usersignup')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
