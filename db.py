import mysql.connector

DB_HOST = "127.0.0.1"
DB_USER = "root"
DB_PASSWORD = "rootpass"
DB_NAME = "sten_sax_pase"
DB_PORT = "3307"


def get_server_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD
    )

# Hej


def get_connection():

    return mysql.connector.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


def init_db():
    server_conn = get_server_connection()
    server_cur = server_conn.cursor()

    server_cur.execute(
        f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"
    )

    server_cur.close()
    server_conn.close()

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""

        CREATE TABLE IF NOT EXISTS rounds (
                id INT AUTO_INCREMENT PRIMARY KEY,
                played_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                player_choice VARCHAR(10) NOT NULL,
                computer_choice VARCHAR(10) NOT NULL,
                result VARCHAR(10) NOT NULL
                )
    """)

    conn.commit()
    cur.close()
    conn.close()



def insert_round(player_choice: str, computer_choice:str, result: str) -> None:
    conn = get_connection()
    cur = conn.cursor()

    print(player_choice, computer_choice, result)

    cur.execute( 
        "INSERT INTO rounds (player_choice, computer_choice, result) VALUES (%s, %s, %s)",
        (player_choice, computer_choice, result)
    )

    conn.commit()
    cur.close()
    conn.close()



def get_stats() -> dict:
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT COUNT(*) FROM rounds")
    total = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM rounds WHERE result = 'vinst'")
    wins = cur.fetchone()[0]

    cur.close()
    conn.close()

    win_percentage = 0 if total == 0 else round((wins/total) * 100)
    return {"total": total, "wins": wins, "win_percentage": win_percentage}