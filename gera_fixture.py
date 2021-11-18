import random
from datetime import date
import json


LENGTH = 12 * 7  # 7 anos

instances = []


for id in range(LENGTH):

    def gera_data(dia):
        return str(date(2015 + (id // 12), (id % 12) + 1, dia))

    instance = {
        'model': 'contas.Conta',
        'pk': id,
        'fields': {
            'data_leitura_relogio': gera_data(10),
            'numero_leitura': 30000 + id,
            'kw': random.randint(50, 1000),
            'valor': round(random.random() * random.randint(40, 1000), 2),
            'data_pagamento': gera_data(1),
            'media_consumo': random.randint(50, 200)
        }
    }
    instances.append(instance)

with open('fixture.json', 'w') as json_file:
    json_file.write(json.dumps(instances, indent=4))
