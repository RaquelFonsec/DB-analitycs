import sqlite3
import os

# Caminho para o diretório do banco de dados
caminho_diretorio = '/home/raquel/Downloads/MeuDBeaver/Dados/'

# Verifica se o diretório existe, se não, cria
if not os.path.exists(caminho_diretorio):
    os.makedirs(caminho_diretorio)

# Caminho completo para o banco de dados
caminho_banco_dados = os.path.join(caminho_diretorio, 'Dados.db')

try:
    # Conecta ao banco de dados
    conexao = sqlite3.connect(caminho_banco_dados)
    cursor = conexao.cursor()

    #  Cria uma tabela chamada "alunos"
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS alunos (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER,
            curso TEXT
        );
    ''')

    # 2. Inserir pelo menos 5 registros de alunos
    alunos_data = [
        (1, 'Aluno1', 22, 'Engenharia'),
        (2, 'Aluno2', 25, 'Ciência da Computação'),
        (3, 'Aluno3', 19, 'Medicina'),
        (4, 'Aluno4', 21, 'Direito'),
        (5, 'Aluno5', 23, 'Administração')
    ]
    cursor.executemany('INSERT INTO alunos VALUES (?, ?, ?, ?)', alunos_data)

    # a) Selecionar todos os registros da tabela "alunos"
    cursor.execute('SELECT * FROM alunos;')
    print("\nTodos os registros da tabela 'alunos':")
    for row in cursor.fetchall():
        print(row)

    # b) Selecionar o nome e a idade dos alunos com mais de 20 anos
    cursor.execute('SELECT nome, idade FROM alunos WHERE idade > 20;')
    print("\nNome e idade dos alunos com mais de 20 anos:")
    for row in cursor.fetchall():
        print(row)

    # c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética
    cursor.execute('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome;')
    print("\nAlunos do curso de 'Engenharia' em ordem alfabética:")
    for row in cursor.fetchall():
        print(row)

    # d) Contar o número total de alunos na tabela
    cursor.execute('SELECT COUNT(*) FROM alunos;')
    total_alunos = cursor.fetchone()[0]
    print(f"\nNúmero total de alunos na tabela: {total_alunos}")

    # a) Atualize a idade de um aluno específico na tabela
    cursor.execute('UPDATE alunos SET idade = 30 WHERE id = 1;')

    # b) Remover um aluno pelo seu ID
    cursor.execute('DELETE FROM alunos WHERE id = 3;')

    # Commit das transações de atualização e remoção
    conexao.commit()

    # Visualização dos dados atualizados
    cursor.execute('SELECT * FROM alunos;')
    print("\nRegistros atualizados na tabela 'alunos':")
    for row in cursor.fetchall():
        print(row)

    # 5. Criar uma Tabela e Inserir Dados
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER,
            saldo REAL
        );
    ''')

    clientes_data = [
        (1, 'Cliente1', 35, 1500.50),
        (2, 'Cliente2', 28, 2000.75),
        (3, 'Cliente3', 40, 1200.00),
        (4, 'Cliente4', 22, 800.50),
        (5, 'Cliente5', 32, 2500.00)
    ]
    cursor.executemany('INSERT INTO clientes VALUES (?, ?, ?, ?)', clientes_data)

    # Commit da transação na tabela de clientes
    conexao.commit()

    
    # a) Selecione o nome e a idade dos clientes com idade superior a 30 anos
    cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
    print("\nNome e idade dos clientes com mais de 30 anos:")
    for row in cursor.fetchall():
        print(row)

    # b) Calcule o saldo médio dos clientes
    cursor.execute('SELECT AVG(saldo) FROM clientes;')
    saldo_medio = cursor.fetchone()[0]
    print(f"\nSaldo médio dos clientes: {saldo_medio:.2f}")

    # c) Encontre o cliente com o saldo máximo
    cursor.execute('SELECT nome, MAX(saldo) FROM clientes;')
    cliente_max_saldo = cursor.fetchone()
    print(f"\nCliente com o saldo máximo: {cliente_max_saldo[0]}, Saldo: {cliente_max_saldo[1]:.2f}")

    # d) Conte quantos clientes têm saldo acima de 1000
    cursor.execute('SELECT COUNT(*) FROM clientes WHERE saldo > 1000;')
    clientes_acima_1000 = cursor.fetchone()[0]
    print(f"\nNúmero de clientes com saldo acima de 1000: {clientes_acima_1000}")

    # 7. Atualização e Remoção com Condições
    # a) Atualize o saldo de um cliente específico
    cursor.execute('UPDATE clientes SET saldo = 2000.00 WHERE id = 1;')

    # b) Remova um cliente pelo seu ID
    cursor.execute('DELETE FROM clientes WHERE id = 3;')

    # Commit das transações de atualização e remoção na tabela de clientes
    conexao.commit()

    # Visualização dos dados atualizados na tabela de clientes
    cursor.execute('SELECT * FROM clientes;')
    print("\nRegistros atualizados na tabela 'clientes':")
    for row in cursor.fetchall():
        print(row)

    # 8. Junção de Tabelas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compras (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            produto TEXT,
            valor REAL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        );
    ''')

    compras_data = [
        (1, 1, 'Produto1', 500.00),
        (2, 2, 'Produto2', 1200.50),
        (3, 3, 'Produto3', 800.00),
        (4, 4, 'Produto4', 300.75),
        (5, 5, 'Produto5', 1500.00)
    ]
    cursor.executemany('INSERT INTO compras VALUES (?, ?, ?, ?)', compras_data)

    # Commit da transação na tabela de compras
    conexao.commit()

    # Consulta para exibir o nome do cliente, o produto e o valor de cada compra
    cursor.execute('''
        SELECT clientes.nome, compras.produto, compras.valor
        FROM clientes
        JOIN compras ON clientes.id = compras.cliente_id;
    ''')
    print("\nNome do cliente, produto e valor de cada compra:")
    for row in cursor.fetchall():
        print(row)

except sqlite3.Error as e:
    print(f"Erro SQLite: {e}")

finally:
    
    if conexao:
        conexao.close()


