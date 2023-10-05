from cassandra.cluster import Cluster

cluster = Cluster(['localhost'])
session = cluster.connect('tasks_keyspace')


session.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id UUID PRIMARY KEY,
        title TEXT,
        description TEXT
    )
""")
from uuid import uuid4

def adicionar_tarefa(titulo, descricao):
    task_id = uuid4()
    session.execute("""
        INSERT INTO tasks (id, title, description)
        VALUES (%s, %s, %s)
    """, (task_id, titulo, descricao))


adicionar_tarefa('Tarefa 1', 'Descrição da Tarefa 1')
def listar_tarefas():
    rows = session.execute("SELECT id, title FROM tasks")
    for row in rows:
        print(f"ID: {row.id}, Título: {row.title}")


listar_tarefas()
def visualizar_descricao_tarefa(titulo):
    rows = session.execute("SELECT id, title, description FROM tasks WHERE title = %s", (titulo,))
    for row in rows:
        print(f"ID: {row.id}, Título: {row.title}, Descrição: {row.description}")


visualizar_descricao_tarefa('Tarefa 1')
def remover_tarefa(task_id):
    session.execute("DELETE FROM tasks WHERE id = %s", (task_id,))


remover_tarefa(task_id)
