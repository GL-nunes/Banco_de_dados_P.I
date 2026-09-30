from sqlalchemy import create_engine, Column, String , Integer, Boolean, ForeignKey #cria o banco de dados
from sqlalchemy.orm import sessionmaker , declarative_base  #declarative_base cria as tabelas do banco de dados e sessionmaker cria seção do banco

db = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind=db)
session = Session() #Inicializa a seção criada


Base = declarative_base() #Vai construir todas as tabelas e criar o banco de dados

#Criação das tabelas 

class Planta(Base):
    __tablename__ = "plantas"
    id = Column("id", Integer, primary_key = True , autoincrement = True, )
    nome = Column("nome", String) #define o nome da coluna e qual tipo de informação que ele pode receber
    familia = Column("família",String)
    genero = Column("gênero",String)

    def __init__(self,nome,familia,genero):
        self.nome = nome
        self.familia = familia
        self.genero = genero

Base.metadata.create_all(bind = db)
planta = Planta(nome = "Duranta - Erecta", familia = "Verbenaceae", genero = "Duranta")
planta2 = Planta(nome="Adenium", familia="Apocynaceae",genero="Adenium")
planta3 = Planta(nome="Psidium guajava L", familia="Myrtaceae", genero="Psidium")
planta4 = Planta(nome="Mangifera indica L", familia="Anacardiaceae", genero="Mangifera")
session.add(planta)
session.add(planta2)
session.add(planta3)
session.add(planta4)
session.commit()

lista_plantas = session.query(Planta).all() #query é uma consulta no banco de dados, all() retorna todos os registros da tabela
print(lista_plantas)

#fazer tabela separada para espécie e imagens
#class Imagens(Base):
#    Url = Column("Url",String,primary_key = True)
#    qtd_imagens = Column("qtd_imagens",Integer,autoincrement=True)
#    planta  = Column("planta",ForeignKey("plantas.id"))
#
#
#    def __init__(self,Url,qtd_imagens,planta):
#        self.Url = Url
#        self.qtd_imagens = qtd_imagens
#        self.planta = planta