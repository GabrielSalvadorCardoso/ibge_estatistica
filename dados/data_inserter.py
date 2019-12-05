import csv
import requests
import json

with open("projecao-rj.csv", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        projecao = {}
        projecao.update({
            "ano": int(row["ano"]),
            "populacao_homens": int(row["populacao_homens"]),
            "populacao_mulheres": int(row["populacao_mulheres"]),
            "nascimentos": int(row["nascimentos"]),
            "obitos": int(row["obitos"]),
            "saldo_migratorio_interno": int(row["saldo_migratorio_interno"]),
            "saldo_migratorio_internacional": int(row["saldo_migratorio_internacional"]),
            "esperanca_vida_homens": float(row["esperanca_vida_homens"].replace(",", ".")),
            "esperanca_vida_mulheres": float(row["esperanca_vida_mulheres"].replace(",", ".")),
            "taxa_mortalidade_infantil_homens": float(row["taxa_mortalidade_infantil_homens"].replace(",", ".")),
            "taxa_mortalidade_infantil_mulheres": float(row["taxa_mortalidade_infantil_mulheres"].replace(",", ".")),
            "geocodigo_unidade_federativa": "33", # hardcoded
            "taxa_crescimento_geometrico": float(row["taxa_crescimento_geometrico"].replace(",", ".")),
            "taxa_bruta_natalidade": float(row["taxa_bruta_natalidade"].replace(",", ".")),
            "taxa_bruta_mortalidade": float(row["taxa_bruta_mortalidade"].replace(",", ".")),
            "taxa_liquida_migracao": float(row["taxa_liquida_migracao"].replace(",", ".")),
            "taxa_fecundidade_total": float(row["taxa_fecundidade_total"].replace(",", "."))
        })
        response = requests.post("http://localhost:8010/api/ibge/estatistica/projecoes/2018", data=json.dumps(projecao), headers={"Content-Type": "application/json"})
        print(response.status_code)

"""
{
	"ano": 2010,
	"populacao_homens": 7785937,
	"populacao_mulheres": 8517251,
	"nascimentos": 213558,
	"obitos": 118313,
	"saldo_migratorio_interno": 4843,
	"saldo_migratorio_internacional": 0,
	"esperanca_vida_homens": 70.28,
	"esperanca_vida_mulheres": 77.96,
	"taxa_mortalidade_infantil_homens": 15.16,
	"taxa_mortalidade_infantil_mulheres": 12.91,
	"geocodigo_unidade_federativa": "33",
	"taxa_crescimento_geometrico": null,
	"taxa_bruta_natalidade": 13.10,
	"taxa_bruta_mortalidade": 7.26,
	"taxa_liquida_migracao": 0.30,
	"taxa_fecundidade_total": 1.59
}
"""