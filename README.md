# Resultados do Script de Banco de Dados SQLite

Este script Python utiliza SQLite para criar e manipular tabelas em um banco de dados. Abaixo estão alguns dos resultados obtidos durante a execução do script:

## Tabela 'alunos'

### Todos os registros da tabela 'alunos':

```plaintext
| id |   nome  | idade |         curso         |
|----|---------|-------|-----------------------|
| 1  | Aluno1  |  22   |      Engenharia       |
| 2  | Aluno2  |  25   | Ciência da Computação |
| 3  | Aluno3  |  19   |       Medicina        |
| 4  | Aluno4  |  21   |        Direito        |
| 5  | Aluno5  |  23   |   Administração       |


Nome e idade dos alunos com mais de 20 anos


|   nome  | idade |
|---------|-------|
| Aluno1  |  22   |
| Aluno2  |  25   |
| Aluno4  |  21   |
| Aluno5  |  23   |


Alunos do curso de 'Engenharia' em ordem alfabética


| id |   nome  | idade |    curso    |
|----|---------|-------|-------------|
| 1  | Aluno1  |  30   | Engenharia  |

Número total de alunos na tabela: 4


Registros atualizados na tabela 'alunos

| id |   nome  | idade |         curso         |
|----|---------|-------|-----------------------|
| 1  | Aluno1  |  30   |      Engenharia       |
| 2  | Aluno2  |  25   | Ciência da Computação |
| 4  | Aluno4  |  21   |        Direito        |
| 5  | Aluno5  |  23   |   Administração       |




Tabela 'clientes'
Nome e idade dos clientes com mais de 30 anos

|   nome    | idade |
|-----------|-------|
| Cliente1  |  35   |
| Cliente3  |  40   |
| Cliente5  |  32   |


Saldo médio dos clientes: 1600.35
Cliente com o saldo máximo: Cliente5, Saldo: 2500.00
Número de clientes com saldo acima de 1000: 4



Registros atualizados na tabela 'clientes

| id |   nome    | idade |  saldo   |
|----|-----------|-------|----------|
| 1  | Cliente1  |  35   | 2000.00  |
| 2  | Cliente2  |  28   | 2000.75  |
| 4  | Cliente4  |  22   |  800.50  |
| 5  | Cliente5  |  32   | 2500.00  |






Tabela 'compras'
Nome do cliente, produto e valor de cada compra


|   nome    |  produto  |  valor  |
|-----------|-----------|---------|
| Cliente1  | Produto1  |  500.00 |
| Cliente2  | Produto2  | 1200.50 |
| Cliente4  | Produto4  |  300.75 |
| Cliente5  | Produto5  | 1500.00 |





