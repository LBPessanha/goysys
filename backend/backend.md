Com uma abordagem voltada para empresas menores e priorizando simplicidade, começaremos o backend de forma mais enxuta, com foco em funcionalidade e fácil manutenção. Assim, podemos começar com uma estrutura básica e expandir conforme necessário. Vou orientar o plano para que ele seja fácil de adaptar e escalar futuramente.

### Plano de Ação para Estruturação Inicial do Back-End

#### 1. **Escolher e Configurar o Banco de Dados**
   - **Sugestão**: Utilizar **SQLite** para iniciar, pois ele é leve e não requer configuração complexa, sendo ideal para desenvolvimento e empresas pequenas. Caso o sistema cresça, migrar para um banco mais robusto, como PostgreSQL, será possível.
   - **Ações**:
     - Configurar o banco de dados SQLite no projeto.
     - Criar um arquivo `database.py` para gerenciar a conexão e criação das tabelas no banco de dados.
     - Exemplo de conexão básica com SQLite usando SQLAlchemy:
       ```python
       from sqlalchemy import create_engine, Column, Integer, String
       from sqlalchemy.ext.declarative import declarative_base
       from sqlalchemy.orm import sessionmaker

       DATABASE_URL = "sqlite:///./goysys.db"
       engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
       SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
       Base = declarative_base()
       ```

#### 2. **Criar Estrutura Básica de Diretórios**
   - **Objetivo**: Organizar o projeto para que seja modular e fácil de manter, mesmo com uma estrutura simplificada.
   - **Ações**:
     - Criar a seguinte estrutura de diretórios:
       ```
       goysys_backend/
       ├── models/           # Modelos de dados
       ├── crud/             # Funções de manipulação de dados
       ├── main.py           # Arquivo principal para execução do back-end
       └── database.py       # Configuração e conexão do banco de dados
       ```

#### 3. **Definir os Modelos de Dados**
   - **Objetivo**: Criar as tabelas essenciais de `Funcionário` e `Cliente`.
   - **Ações**:
     - Em `models/`, criar os modelos para Funcionário e Cliente utilizando SQLAlchemy.
     - Exemplo básico para o modelo `Funcionario`:
       ```python
       from sqlalchemy import Column, Integer, String
       from database import Base

       class Funcionario(Base):
           __tablename__ = "funcionarios"
           id = Column(Integer, primary_key=True, index=True)
           nome = Column(String, index=True)
           cargo = Column(String)
           # outros campos relevantes

       class Cliente(Base):
           __tablename__ = "clientes"
           id = Column(Integer, primary_key=True, index=True)
           nome = Column(String, index=True)
           # outros campos relevantes
       ```
     - Executar a criação das tabelas no banco com `Base.metadata.create_all(bind=engine)` dentro do `database.py`.

#### 4. **Implementar Funções CRUD Simples**
   - **Objetivo**: Fornecer operações básicas de CRUD para Funcionários e Clientes.
   - **Ações**:
     - Criar funções CRUD em `crud/funcionarios.py` e `crud/clientes.py`.
     - Exemplo de função de criação para `Funcionario`:
       ```python
       from sqlalchemy.orm import Session
       from models import Funcionario

       def criar_funcionario(db: Session, nome: str, cargo: str):
           novo_funcionario = Funcionario(nome=nome, cargo=cargo)
           db.add(novo_funcionario)
           db.commit()
           db.refresh(novo_funcionario)
           return novo_funcionario
       ```

#### 5. **Criar um Arquivo `main.py` para Rodar o Back-End**
   - **Objetivo**: Criar um ponto de entrada para o back-end, utilizando um framework leve, como **FastAPI**, para expor as operações CRUD por meio de uma API REST.
   - **Ações**:
     - Criar o arquivo `main.py` com uma estrutura básica do FastAPI:
       ```python
       from fastapi import FastAPI, Depends
       from sqlalchemy.orm import Session
       from database import SessionLocal, engine
       import crud

       app = FastAPI()

       def get_db():
           db = SessionLocal()
           try:
               yield db
           finally:
               db.close()

       @app.post("/funcionarios/")
       def criar_funcionario(nome: str, cargo: str, db: Session = Depends(get_db)):
           return crud.criar_funcionario(db, nome=nome, cargo=cargo)
       ```

#### 6. **Testes Manuais e Ajustes**
   - **Objetivo**: Testar as operações CRUD para verificar se estão funcionando corretamente.
   - **Ações**:
     - Usar **curl** ou uma ferramenta de API (como Postman ou Insomnia) para testar as rotas da API.
     - Verificar se os dados de Funcionários e Clientes estão sendo criados e lidos corretamente no banco de dados.

Esse plano estabelece uma estrutura inicial que é simples, mas preparada para expansão. Começar com SQLite e um CRUD básico permite que o sistema esteja funcional rapidamente, com a possibilidade de aprimorar e escalar caso as necessidades da empresa aumentem.