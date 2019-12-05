from rest_framework.serializers import ModelSerializer
from .models import *

class EstacaoSerializer(ModelSerializer):
    class Meta:
        model = Projecao
        id_field = 'id'
        fields = [
            'id',
            'ano',
            'populacao_homens',
            'populacao_mulheres',
            'nascimentos',
            'obitos',
            'saldo_migratorio_interno',
            'saldo_migratorio_internacional',
            'esperanca_vida_homens',
            'esperanca_vida_mulheres',
            'taxa_mortalidade_infantil_homens',
            'taxa_mortalidade_infantil_mulheres',
            'geocodigo_unidade_federativa',
            'taxa_crescimento_geometrico',
            'taxa_bruta_natalidade',
            'taxa_bruta_mortalidade',
            'taxa_liquida_migracao',
            'taxa_fecundidade_total',
        ]