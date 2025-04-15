# Generated by Django 5.2 on 2025-04-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submit_form', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceClaim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('policy_number', models.CharField(max_length=100)),
                ('claim_type', models.CharField(max_length=30)),
                ('incident_date', models.DateField()),
                ('description', models.TextField()),
                ('claim_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('supporting_document', models.FileField(upload_to='claims/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Submission',
        ),
    ]
