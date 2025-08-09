import sqlite3
import os


# Configuração do banco de dados
DB_NAME = 'user_database_secure.db'

def get_db_connection():
    # Cria diretório para o banco de dados se não existir
    os.makedirs('secure_data', exist_ok=True)
    db_path = os.path.join('secure_data', DB_NAME)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    
    try:
        # Tabela de usuários
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

    
    except sqlite3.Error as e:
        print(f"Erro ao inicializar o banco de dados: {e}")
        
    finally:
        conn.close()

# Inicializa o banco de dados ao importar o módulo
init_db()

class Database:
    def __init__(self, username, email, password):
        self.user = username
        self.email = email
        self.password = password

    def insert_user(self):
        conn = get_db_connection()
        try:
            conn.execute('''
                INSERT INTO users (username, email, password)
                VALUES (?, ?, ?)
            ''', (self.user, self.email, self.password))
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao inserir usuário: {e}")
            conn.rollback()
            return False
        finally:
            conn.close()

    def get_email_by_user(self):
        conn = get_db_connection()
        try:
            cursor = conn.execute('''
                SELECT email FROM users WHERE username = ?
            ''', (self.user,))
            user = cursor.fetchone()
            return user
        except sqlite3.Error as e:
            print(f"Erro ao buscar email: {e}")
            return None
        finally:
            conn.close()

    def verify_password(self):
        conn = get_db_connection()
        try:
            email_row = self.get_email_by_user()

            if email_row is None:
                print("Erro ao buscar email.")
                return None

            email = email_row['email']

            cursor = conn.execute('''
                SELECT * FROM users WHERE email = ? AND password = ?
            ''', (email, self.password))
            resultado = cursor.fetchone()
            return True if resultado else False

        except sqlite3.Error as e:
            print(f"Erro ao verificar senha: {e}")
            return None
        
        finally:
            conn.close()

