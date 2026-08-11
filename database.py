import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class BancoRAD:
    def conectar(self):
        try:
            self.conexao = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT")
            )
            self.cursor = self.conexao.cursor()
        except Exception as erro:
            print("Erro ao conectar:", erro)

    def inserir(self, aluno_nome, matricula, tipo, prioridade, status, descricao, prazo):
        try:
            self.cursor.execute(
                "INSERT INTO solicitacoes_rad "
                "(aluno_nome, matricula, tipo_solicitacao, "
                "prioridade, status, descricao, prazo) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                (
                    aluno_nome,
                    matricula,
                    tipo,
                    prioridade,
                    status,
                    descricao,
                    prazo
                )
            )
            self.conexao.commit()
        except Exception as erro:
            self.conexao.rollback()
            print("Erro ao inserir:", erro)

    def listar(self):
        try:
            self.cursor.execute("SELECT * FROM solicitacoes_rad")
            return self.cursor.fetchall()
        except Exception as erro:
            self.conexao.rollback()
            print("Erro ao listar:", erro)

    def pesquisar(self, termo):
        try:
            termo_busca = f"%{termo}%"
            sql = """
            SELECT * FROM solicitacoes_rad 
            WHERE aluno_nome ILIKE %s 
            OR status ILIKE %s 
            OR prioridade ILIKE %s
            """
            self.cursor.execute(sql, (termo_busca, termo_busca, termo_busca))
            return self.cursor.fetchall()
        except Exception as erro:
            self.conexao.rollback()
            print("Erro ao pesquisar:", erro)

    def atualizar(self, id_registro, aluno_nome, matricula, tipo,
                  prioridade, status, descricao, prazo):
        try:
            self.cursor.execute(
                "UPDATE solicitacoes_rad SET aluno_nome = %s, matricula = %s, tipo_solicitacao = %s, "
                "prioridade = %s, status = %s, descricao = %s, prazo = %s WHERE id = %s",
                (
                    aluno_nome,
                    matricula,
                    tipo,
                    prioridade,
                    status,
                    descricao,
                    prazo,
                    id_registro
                )
            )
            self.conexao.commit()
        except Exception as erro:
            self.conexao.rollback()
            print("Erro ao atualizar:", erro)

    def excluir(self, id_registro):
        try:
            self.cursor.execute(
                "DELETE FROM solicitacoes_rad WHERE id = %s",
                (id_registro,)
            )
            self.conexao.commit()
        except Exception as erro:
            self.conexao.rollback()
            print("Erro ao deletar:", erro)