## API Python - Flask - MVC

Projeto de uma API REST, baseado em Python - Flask, usando uma conexão com banco de dados Mysql. 

O projeto é baseado em paradigma orientado a objetos, sob a perspectiva SOLID, valorizando um conjunto de boas práticas na escrita de software, Clean Code, convenções como PEP 8 – Guia de Estilo para Código Python.

Este Projeto API REST, é parte de um segundo projeto, que é um CRUD, e utilizam o mesmo banco de dados mysql. 

Poderiam estar juntos, como um projeto somente, mas para fins didáticos e de boas práticas, ficam separados, para melhor observação de sua arquitetura, boas práticas e de sua evolução.

## Comandos Básicos do Projeto

#### Você deve ter instalado em seu ambiente o Mysql


#### Instale o mysql:

    sudo apt install mysql-server -y

Inicia mysql

    sudo systemctl start mysql
    
    sudo systemctl enable mysql  
    
Acesse o MySQL como root (sem senha, na primeira vez):

    sudo mysql  

Dentro do prompt do MySQL, defina a senha do usuário root como cbv123:

    ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'cbv123';  
    
Atualize os Privilegios

    FLUSH PRIVILEGES;  
    
Crie o Banco carros

    CREATE DATABASE carros;  
    
 Saia do Mysql

    EXIT;  

## Criar ambiente

#### Criar ambiente

    python3 -m venv venv

#### Ativar ambiente Linux MacOs

    source ./venv/bin/activate

#### Ativar ambiente Windows

    myenv\Scripts\activate

#### Instalar dependências

    pip3 install -r requirements.txt

#### Rodar

    python3 run.py


#### Fonte:

https://www.youtube.com/watch?v=vgPC7RZ5UJc

https://www.youtube.com/watch?v=LP8besicfH4

https://peps.python.org/pep-0008/

https://drive.google.com/file/d/0B9eZlIWAs3-sN3NRbktQNVFUN3l2cTBBcXN4Y3FaUQ/view
