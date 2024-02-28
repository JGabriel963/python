# Generated by Django 5.0.2 on 2024-02-28 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clube',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('ano_fundacao', models.PositiveIntegerField(help_text='Ano que o Clube foi criado', verbose_name='Ano Fundação')),
                ('divisao', models.CharField(choices=[('A', 'Série A'), ('B', 'Série B'), ('C', 'Série C'), ('D', 'Série D')], default='D', max_length=60, null=True, verbose_name='Divisão')),
                ('modalidade', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], default='M', max_length=10)),
            ],
        ),
    ]