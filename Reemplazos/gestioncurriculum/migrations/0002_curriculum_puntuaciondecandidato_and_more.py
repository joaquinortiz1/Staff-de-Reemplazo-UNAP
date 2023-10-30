# Generated by Django 4.2.4 on 2023-10-09 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestioncurriculum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('experience', models.TextField()),
                ('skills', models.TextField()),
                ('education', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='PuntuacionDeCandidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioncurriculum.curriculum')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudDeReemplazo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('password1', models.CharField(max_length=128)),
                ('password2', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='Candidato',
        ),
        migrations.DeleteModel(
            name='Vacante',
        ),
        migrations.AddField(
            model_name='solicituddereemplazo',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='solicitudes_de_reemplazo', to='gestioncurriculum.usuario'),
        ),
        migrations.AddField(
            model_name='puntuaciondecandidato',
            name='solicitud_de_reemplazo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioncurriculum.solicituddereemplazo'),
        ),
        migrations.AddField(
            model_name='curriculum',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestioncurriculum.usuario'),
        ),
    ]
