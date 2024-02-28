# Generated by Django 5.0.2 on 2024-02-28 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soccer', '0002_alter_clube_ano_fundacao_jogador'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clube',
            options={'verbose_name': 'Clube', 'verbose_name_plural': 'Clubes'},
        ),
        migrations.AlterField(
            model_name='clube',
            name='divisao',
            field=models.CharField(choices=[('A', 'Série A'), ('B', 'Série B'), ('C', 'Série C'), ('D', 'Série D'), ('S', 'Sem Série')], default='S', max_length=60, null=True, verbose_name='Divisão'),
        ),
    ]
