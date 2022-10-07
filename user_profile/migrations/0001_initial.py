# Generated by Django 3.2 on 2022-10-04 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=16)),
                ('account_type', models.CharField(choices=[('admin', 'Admin'), ('manager', 'Manager'), ('receptionist', 'Receptionist'), ('guest', 'Guest'), ('stuff', 'Stuff')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('zip_code', models.IntegerField()),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_profile.person')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=16)),
                ('status', models.BooleanField(default=True)),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='user_profile.person')),
            ],
        ),
    ]