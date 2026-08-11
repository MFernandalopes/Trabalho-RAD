from database import BancoRAD
import random
from faker import Faker

fake = Faker('pt_BR')


banco = BancoRAD()
banco.conectar()

tipos = ["Dúvida", "Entrega", "Correção", "Orientação", "Revisão", "Outro"]
prioridades = ["Baixa", "Média", "Alta"]
status_opcoes = ["Aberto", "Em andamento", "Concluído", "Cancelado"]



for i in range(20):
    aluno_nome = fake.name()
    matricula = str(random.randint(10000, 99999))
    tipo = random.choice(tipos)
    prioridade = random.choice(prioridades)
    status = random.choice(status_opcoes)
    descricao = fake.sentence()
    prazo = fake.date_this_year()

    banco.inserir(aluno_nome, matricula, tipo, prioridade, status, descricao, prazo)


