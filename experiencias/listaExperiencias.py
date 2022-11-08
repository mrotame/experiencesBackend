class ListaExperiencias():
    todas = [
            {
                "nome":"AppNote",
                "subnome":"Freelancer",
                "desc":"""
                    Projetei e desenvolvi, como freelancer, uma aplicação web de Anotações semelhante ao OneNote da Microsoft para ser implementada em uma plataforma web do cliente
                    Desenvolvi a API com arquitetura REST utilizando Flask (Python)
                    Utilizei PostgreSQL e MongoDB via ORM para gerenciamento de usuários e documentos
                    Garanti a segurança do sistema utilizando testes unitários nas partes centrais do projeto
                    Utilizei HTML5, CSS3, Javascript e React Vite (NodeJS) para o front-end.
                    Implantei a aplicação no sistema do cliente hospedado na Salesforce Heroku
                """,
                "data_inicio":"2018/01",
                "data_fim":"2018/03",
                "tags":['python','flask','rest','js','javascript','html','html5',"react","node","fullstack","heroku"]
            },
            {
                "nome":"VansApp",
                "subnome":"Nest",
                "desc":"""
                    Liderei uma equipe de profissionais e participei ativamente do desenvolvimento de uma plataforma web móvel para gerenciamento de ônibus fretados.
                    Realizei uma pesquisa interna com clientes da plataforma para arquitetar o projeto de forma estruturada utilizando conceitos conhecidos do UML
                    O MVC da aplicação foi desenvolvida utilizando Flask, servindo arquivos estaticos (HTML, CSS, JS), e posteriormente, após a validação, Migrei a aplicação front e back-end para o framework Django (Python)
                    Supervisionei o desenvolvimento do banco de dados SQL e NO-SQL e implantei os bancos no sistema utilizando o ORM Django-DB e Pymongo
                    Migrei a aplicação web para android utilizando Cordova/Phonegap (NodeJs).
                    Auxiliei a implantação do sistema no Google Cloud App Engine, e Google Firebase
                """,
                "data_inicio":"2017/01",
                "data_fim":"2019/01",
                "tags":['python','flask','django',"node","orm","sql","nosql","uml","cordova","phonegap","mobile","android","gcloud","cloud"]
            },
            {
                "nome":"Automação web & web scrapping para obtenção de dados de imóvel do município de Aparecida",
                "subnome":"Compila",
                "desc":"""
                    Projetei e desenvolvi uma aplicação capaz de acessar serviços municipais de consulta de IPTUs, coletar dados detalhados do imóvel e das parcelas, além de baixar e processar individualmente os boletos das parcelas.
                    A aplicação foi integrada a uma API REST, no qual os clientes poderiam acessar informando dados do ímovel, e receberiam todas as informações sobre o imóvel solicitado, incluindo todas as parcelas em aberto do IPTU.
                    A API foi inteiramente desenvolvida utilizando Flask (Python)
                    A busca e coleta dos dados nos serviços municipais foi desenvolvida utilizando o framework Selenium
                    Para o controle de arquivos e versionamento do projeto foi utilizado o serviço GIT, e para os testes e validação do sistema, foi utilizado de conteinerização Docker para garantir.
                    Implantei a aplicação final na AWS EC2
                """,
                "data_inicio":"2020/06",
                "data_fim":"2020/06",
                "tags":["python","flask","rest","api","automatização","scrapping","selenium","docker","git","aws","ec2"]
            },
            {
                "nome":"Bot de extração de dados de Notas Fiscais de Serviço Eletrônica",
                "subnome":"Compila",
                "desc":"""
                    Projetei e desenvolvi uma aplicação capaz processar diariamente milhares de notas fiscais de serviço aletronicas (NFSe) em PDFs, extrair informações, processa-las e persisti-las em umabase de dados NoSql MongoDB (futuramente migrada para Postgresql).
                    A extração dos dados foi preparada utilizando um sistema de layouts, para comportas as diferenças do modelo da nota de cada município. 
                    A aplicação foi desenvolvida de forma escalavel à facilitar o desenvolvimento e incremento de novos templates e municípios, além de comportar novos e multiplos bancos de dados simultaneos, conforme a necessidade da escalabilidade da aplicação.
                    Para facilitar o desenvolvimento de novos templates e integração de novos municípios, desenvolvi um CLI que automaticamente cria todas as pastas e arquivos prontas para implementação, e já integra à aplicação, alterando diretamente as classes de listagem da aplicação para importar e implementar o novo template criado.
                """,
                "data_inicio":"2022/06",
                "data_fim":"2022/07",
                "tags":["bot","flask","municipal","nfse", "mongodb", "pdf", "scrapping", "postgresql", "CLI"]
            },
            {
                "nome":"Desenvolvimento de sistema ERP auxiliar",
                "subnome":"Compila",
                "desc":"""
                    Projetei e desenvolvi por conta propria um sistema escalavel inteiro utilizado por milhares de usuarios, apartir de um MVC desenvolvido anteriormente.
                    o sistema constituiu de uma junção de varias aplicações, de APIs restful à JOBs de micro-serviços de consulta e monitoramento de solicitações, encaminhamento, processamento e validação de dados, consulta e persistencia de informações em base de dados Postgresql.
                    As APIs restful foram desenvolvidas inteiramente em Python, utilizando diversas bibliotecas diferentes para cada aplicação do sistema, conforme a sua função. A validação das requests em JSON foram realizadas através da biblioteca Cerberus
                    A banco foi desenvolvido de maneira evolutiva utilizando de migrações através da biblioteca Alembic, e a conexão ao banco de dados foi realizada utilizando ORMs através da biblioteca SQLAlchemy
                    Todo o código do sistema foi armazenado nos servidores GIT da AWS Code commit da empresa.
                    A Implantação final foi feita na AWS em uma instancia Linux da EC2, utilizando o PM2 para o gerenciamento isolado de cada aplicação do sistema.
                """,
                "data_inicio":"2022/07",
                "data_fim":"",
                "tags":["python", "flask", "api","rest", "git", "aws","ec2","codecommit","PM2","postgres", 'alembic', 'sqlalchemy','orms', 'escalavel', 'cerberus']
            },
            {
                "nome":"Replicador Git",
                "subnome":"Projeto Proprio",
                "desc": """
                    Projetei e desenvolvi, a partir de uma necessidade interna, uma mini-aplicação capaz de replicar um projeto em vários servidores GITs, sem a necessidade de precisar realizar commits e pushs em casa servidor individualmente. Ao realizar um commit em um servidor, a aplicação que monitora o repositório mestre automaticamente replica as alterações em todos os outros servidores/repositórios GIT.
                    O projeto foi desenvolvido exclusivamente em Python e implantado em uma instancia Compute Engine da GCP (Google Cloud Platform)
                """,
                "data_inicio":"2022/08",
                "data_fim":"2022/08",
                "tags": ["python","gcloud","git"]
            }
            
        ]