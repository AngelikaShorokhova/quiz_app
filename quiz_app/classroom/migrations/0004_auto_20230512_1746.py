# Generated by Django 2.0.1 on 2023-05-12 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0003_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='classroom.Group'),
        ),
        migrations.AddField(
            model_name='student',
            name='name',
            field=models.CharField(default=1, max_length=255, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
