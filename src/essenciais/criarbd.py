import psycopg2
from psycopg2 import sql
from psycopg2 import errors
def criarBD():
    # PARAMETROS PARA SE CONECTAR AO BD POSTGRES
    conn_params = {
        'host': '127.0.0.1',
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '123'
    }

    # CODIGO SQL PARA SER EXECUTADO MAIS A FRENTE
    departamentos = (
        """
        CREATE TABLE IF NOT EXISTS departamentos (
            id_departamento SERIAL PRIMARY KEY,
            nome_departamento VARCHAR(100) NOT NULL
        );

        INSERT INTO departamentos (nome_departamento)
        VALUES ('Administrativo');

        INSERT INTO departamentos (nome_departamento)
        VALUES ('Financeiro');

        INSERT INTO departamentos (nome_departamento)
        VALUES ('RH');

        INSERT INTO departamentos (nome_departamento)
        VALUES ('Comercial');

        INSERT INTO departamentos (nome_departamento)
        VALUES ('TI');

        INSERT INTO departamentos (nome_departamento)
        VALUES ('Produção');

        INSERT INTO departamentos (nome_departamento)
        VALUES ('Jurídico');
        """
    )
    cargos = (
        """
        CREATE TABLE IF NOT EXISTS cargos (
            id_cargo SERIAL PRIMARY KEY,
            nome_cargo VARCHAR(100) NOT NULL,
            salario_cargo NUMERIC(10,2) NOT NULL
        );

        INSERT INTO cargos (nome_cargo,salario_cargo)
        VALUES ('Presidência',23531.16);

        INSERT INTO cargos (nome_cargo,salario_cargo)
        VALUES ('Diretoria',16513.89);

        INSERT INTO cargos (nome_cargo,salario_cargo)
        VALUES ('Gerência',11189.40);

        INSERT INTO cargos (nome_cargo,salario_cargo)
        VALUES ('Supervisão',7087.80);

        INSERT INTO cargos (nome_cargo,salario_cargo)
        VALUES ('Analista',5217.89);

        INSERT INTO cargos (nome_cargo,salario_cargo)
        VALUES ('Assistente',3621.52);

        INSERT INTO cargos (nome_cargo,salario_cargo)
        VALUES ('Auxiliar',1650.31);
        """
    )
    funcionarios = (
        """
        CREATE TABLE IF NOT EXISTS funcionarios (
            id_funcionario SERIAL PRIMARY KEY,
            nome_funcionario VARCHAR(100) NOT NULL,
            cpf VARCHAR(11) NOT NULL,
            endereco VARCHAR(100),
            telefone VARCHAR(11),
            id_departamento INT NOT NULL,
            id_cargo INT NOT NULL,
            FOREIGN KEY (id_departamento) REFERENCES departamentos (id_departamento),
            FOREIGN KEY (id_cargo) REFERENCES cargos (id_cargo)
        );

        INSERT INTO funcionarios (nome_funcionario,cpf,endereco,telefone,id_cargo,id_departamento)
        VALUES ('Lucas','00000101010','Avenida alguma coisa','2140028922',5,5);

        INSERT INTO funcionarios (nome_funcionario,cpf,endereco,telefone,id_cargo,id_departamento)
        VALUES ('Danilo','12345678900','Rua das flores','21912345678',3,4);

        INSERT INTO funcionarios (nome_funcionario,cpf,endereco,telefone,id_cargo,id_departamento)
        VALUES ('João','56714515104','Rua Alguma coisa','21912345678',2,3);

        INSERT INTO funcionarios (nome_funcionario,cpf,endereco,telefone,id_cargo,id_departamento)
        VALUES ('Carlos','98765432101','Rua Alguma coisa','21912345678',1,5);

        INSERT INTO funcionarios (nome_funcionario,cpf,endereco,telefone,id_cargo,id_departamento)
        VALUES ('Irineu','10293847560','Rua dos bobos','21912345678',6,7);
        """
    )

    connection = None

    # O CODIGO DE FATO PARA CRIAÇÃO DO BANCO DE DADOS, TABELAS E ITENS DAS TABELAS CASO JÁ NÃO EXISTAM
    try:
        # CONECTANDO AO BD PADRÃO DO POSTGRESQL
        connection = psycopg2.connect(**conn_params)
        connection.autocommit = True  # Necessário para executar a criação do banco de dados
        
        # CRIAÇÃO DO CURSOR
        cursor = connection.cursor()
        
        # CODIGO PARA VER SE O BANCO DE DADOS DO NOME ESCOLHIDO JA EXISTE
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = %s;", ("e-enterprise",))
        
        # CONFIRMANDO QUE ELE NÃO EXISTE ELE É CRIADO
        if (cursor.fetchone() == None):
            cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("e-enterprise")))

        # FECHA A CONEXÃO COM O BD POSTGRES
        connection.close()


        # ABRE A CONEXÃO COM O NOSSO BANCO DE DADOS PARA INSERIR OS DADOS BASE DO PROJETO
        conn_params['dbname'] = 'e-enterprise'  # Atualiza o nome do banco de dados
        connection = psycopg2.connect(**conn_params)
        cursor = connection.cursor()

        # VENDO SE A TABELA DE DEPARTAMENTOS JA EXISTE
        cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'departamentos'
        );
        """)
        tabela_existe = cursor.fetchone()[0]
        # SE ELA NÃO EXISTIR É CRIADA E POPULADA
        if (tabela_existe == False):
            cursor.execute(departamentos)
        
        # VENDO SE A TABELA DE CARGOS JA EXISTE
        cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'cargos'
        );
        """)
        tabela_existe = cursor.fetchone()[0]
        # SE ELA NÃO EXISTIR É CRIADA E POPULADA
        if (tabela_existe == False):
            cursor.execute(cargos)

        # VENDO SE A TABELA DE FUNCIONARIOS JA EXISTE
        cursor.execute("""
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = 'funcionarios'
        );
        """)
        tabela_existe = cursor.fetchone()[0]
        # SE ELA NÃO EXISTIR É CRIADA E POPULADA
        if (tabela_existe == False):
            cursor.execute(funcionarios)

        # DANDO COMMIT NAS MUDANÇAS FEITAS(Criação e populando as tabelas)
        connection.commit() 
            
    except psycopg2.Error as error:
        print(f"Erro ao conectar ao banco de dados: {error}")
        
    finally:
        # Fecha a conexão
        if(connection != None):
            connection.close()