# Generated by Django 3.2.22 on 2023-12-05 13:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cost', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PLANNED', 'Planned'), ('COMPLETED', 'Completed'), ('CANCELED', 'Canceled')], max_length=20)),
                ('notes', models.TextField(null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visit.schedule')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='visit.service')),
            ],
        ),
    ]
