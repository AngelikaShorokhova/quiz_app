# Generated by Django 2.2.7 on 2023-05-14 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0011_message_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='taken_quizzes', to='classroom.Room'),
        ),
    ]
