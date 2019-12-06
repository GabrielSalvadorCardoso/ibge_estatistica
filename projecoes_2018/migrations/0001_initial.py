# Generated by Django 2.2.3 on 2019-10-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estacao',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ano', models.IntegerField()),
                ('populacao_homens', models.IntegerField()),
                ('populacao_mulheres', models.IntegerField()),
                ('nascimentos', models.IntegerField()),
                ('obitos', models.IntegerField()),
                ('saldo_migratorio_interno', models.IntegerField()),
                ('saldo_migratorio_internacional', models.IntegerField()),
                ('esperanca_vida_homens', models.FloatField()),
                ('esperanca_vida_mulheres', models.FloatField()),
                ('taxa_mortalidade_infantil_homens', models.FloatField()),
                ('taxa_mortalidade_infantil_mulheres', models.FloatField()),
                ('geocodigo_unidade_federativa', models.CharField(max_length=2)),
                ('taxa_crescimento_geometrico', models.FloatField()),
                ('taxa_bruta_natalidade', models.FloatField()),
                ('taxa_bruta_mortalidade', models.FloatField()),
                ('taxa_liquida_migracao', models.FloatField()),
                ('taxa_fecundidade_total', models.FloatField()),
            ],
            options={
                'db_table': 'estacao',
                'managed': True,
            },
        ),
    ]