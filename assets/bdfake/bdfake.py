# cria um banco de dados fake, para testarmos as funcionalidades
# salvar os arquivos gerados na pasta bd-fake

import pandas as pd
from faker import Faker

# Inicializar Faker para dados aleatórios
fake = Faker('pt_BR')

# Gerar dados para funcionários
funcionarios = [
    {
        'ID': i + 1,
        'Nome': fake.name(),
        'CPF': fake.cpf(),
        'RG': fake.rg(),
        'Cargo': fake.job(),
    }
    for i in range(5) # inserir a quantidade de funcionarios
]

# Gerar dados para clientes
clientes = [
    {
        'ID': i + 1,
        'Nome': fake.name(),
        'CPF/CNPJ': fake.cpf() if i % 2 == 0 else fake.cnpj(),
        'Endereço': fake.address().replace('\n', ', '),
        'Cliente desde': f"{fake.month():02d}/{fake.year()}"
    }
    for i in range(25) # inserir a quantidade de clientes
]

# Criar DataFrames
df_funcionarios = pd.DataFrame(funcionarios)
df_clientes = pd.DataFrame(clientes)

# Salvar em CSVs
funcionarios_csv = "/mnt/data/funcionarios.csv"
clientes_csv = "/mnt/data/clientes.csv"

df_funcionarios.to_csv(funcionarios_csv, index=False, encoding='utf-8')
df_clientes.to_csv(clientes_csv, index=False, encoding='utf-8')

funcionarios_csv, clientes_csv
