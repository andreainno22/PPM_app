# Generated by Django 4.2.1 on 2023-06-10 09:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitnessApp', '0016_alter_customuser_calories_burned_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='UserExercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_weight', models.PositiveIntegerField(default=1, null=True)),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitnessApp.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='workoutexercise',
            name='user_exercise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='fitnessApp.userexercise'),
        ),
    ]
