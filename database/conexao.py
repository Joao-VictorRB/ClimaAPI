import sqlite3

conexão = sqlite3.connect('clima.db')
cursor = conexão.cursor()


cursor.execute('''
        CREATE TABLE IF NOT EXISTS cidades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        latitude REAL,
        longitude REAL
        )
    ''')

cursor.execute('''
        CREATE TABLE IF NOT EXISTS previsoes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cidade_id INTEGER NOT NULL,
        data_hora TEXT,
        temperatura REAL,
        sensacao_termica REAL,
        umidade INTEGER,
        pressao INTEGER,
        clima TEXT,
        descrição TEXT,
        vento REAL,
        FOREIGN KEY (cidade_id) REFERENCES cidades (id)
        )
    ''')



def salvar_previsao(clima):
    conexao = sqlite3.connect('clima.db')
    cursor = conexao.cursor()

    cursor.execute('SELECT id FROM cidades WHERE nome = ?', (clima['cidade'],))
    cidade_resultado = cursor.fetchone()

    if cidade_resultado:
        cidade_id = cidade_resultado[0]
    else:
        cursor.execute(
            'INSERT INTO cidades (nome, latitude, longitude) VALUES (?, ?, ?)',
            (clima['cidade'], clima['latitude'], clima['longitude'])
        )
        cidade_id = cursor.lastrowid

    cursor.execute('''
        INSERT INTO previsoes (cidade_id, data_hora, temperatura, sensacao_termica, umidade, pressao, clima, descrição, vento)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        cidade_id,
        clima['data_hora'],
        clima['temperatura'],
        clima['sensacao_termica'],
        clima['umidade'],
        clima['pressao'],
        clima['clima'],
        clima['descricao'],
        clima['vento']
    ))
    
    conexao.commit()
    conexao.close()

    return {
        'cidade': clima['cidade'],
        'temperatura': clima['temperatura'],
        'sensacao_termica': clima['sensacao_termica'],
        'umidade': clima['umidade'],
        'pressao': clima['pressao'],
        'clima': clima['clima'],
        'descricao': clima['descricao'],
        'vento': clima['vento']
    }