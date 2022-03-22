import sqlite3

# Classe Banco de dados
class Database:
    
    # Função de inicialização do banco de dados.
    def __init__(self): 
        
        self.conn = sqlite3.connect('db/database.db')   # Conexão ao arquivo do banco de dados ou criando o arquivo caso ainda não exista.
        self.cursor = self.conn.cursor()                # Cursor para manipulação do banco.        


    # Criando a tabela e adicionando as colunas.
    def create(self):
        
        # Comando SQL para criar tabela com colunas id, generation, balance.
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS best_traders_balances 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, 
            generation TEXT, 
            balance TEXT);
            ''')
        self.conn.commit()

    
    def insert(self, generation, balance):
        # Inserindo os dados no banco.
        self.cursor.execute("INSERT INTO best_traders_balances(generation, balance) VALUES(?,?);",(generation, balance))
        self.conn.commit()

    
    def select(self):
        # Retornando todos os dados da tabela.
        return self.cursor.execute("SELECT * FROM best_traders_balances")
        

        

#######################################################################################################################################
