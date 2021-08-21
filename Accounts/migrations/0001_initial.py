# Generated by Django 3.2.6 on 2021-08-20 13:29

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='usersignup',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('email_token', models.CharField(blank=True, max_length=100, null=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('forgetpass_token', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'Account',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
