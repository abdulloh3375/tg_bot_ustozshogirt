# Generated by Django 5.0.6 on 2024-05-08 16:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('organization', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('full_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('student_type', models.CharField(choices=[('bachalar', 'Bachalar'), ('magister', 'Magister')], default='bachalar', max_length=50)),
                ('contract', models.DecimalField(decimal_places=2, max_digits=8, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentSponsor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sponsor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.sponsor')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.student')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='student',
            name='university',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.university'),
        ),
    ]
