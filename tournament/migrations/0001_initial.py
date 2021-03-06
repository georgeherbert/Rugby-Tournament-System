# Generated by Django 2.1.7 on 2019-03-06 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organiser', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='PitchInstance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
                ('pitches', models.IntegerField()),
                ('halfDuration', models.IntegerField()),
                ('halfTimeDuration', models.IntegerField()),
                ('swapTeamsDuration', models.IntegerField()),
                ('startDate', models.DateField()),
                ('startTime', models.TimeField()),
            ],
        ),
        migrations.AddField(
            model_name='timeslot',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament'),
        ),
        migrations.AddField(
            model_name='pitchinstance',
            name='timeslot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Timeslot'),
        ),
        migrations.AddField(
            model_name='game',
            name='pitch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.PitchInstance'),
        ),
        migrations.AddField(
            model_name='game',
            name='team1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='team.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='team2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='team.Team'),
        ),
        migrations.AddField(
            model_name='enrollment',
            name='tournament',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tournament.Tournament'),
        ),
    ]
