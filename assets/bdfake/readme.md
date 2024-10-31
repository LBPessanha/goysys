# bdfaker.py

Este script, `bdfaker.py`, gera um banco de dados fictício para auxiliar em testes e desenvolvimento, criando dados de exemplo para **funcionários** e **clientes**.

## Estrutura do Banco de Dados

- **Funcionários**: Inclui campos como `ID`, `Nome`, `CPF`, `RG` e `Cargo`.
- **Clientes**: Inclui campos como `ID`, `Nome`, `CPF/CNPJ`, `Endereço` e `Cliente desde` (data de adesão).

## Local de Armazenamento

Os arquivos CSV gerados são salvos na pasta `assets/bdfake`, prontos para serem utilizados em simulações e desenvolvimento.

## Como Executar

1. Certifique-se de ter o ambiente configurado com as dependências necessárias.
2. Execute o script com o comando:

   ```bash
   python bdfaker.py
   ``` 