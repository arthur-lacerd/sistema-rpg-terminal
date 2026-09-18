# RPG Terminal com Base de Dados (em desenvolvimento)

Sistema de RPG por turnos em terminal, com criação de personagens e sistema de batalha com habilidades e traços únicos, junto de um banco de dados que armazena personagens, itens, habilidades e classes. O projeto aplica Programação Orientada a Objetos, utilizando a biblioteca sqlite3 para controle de dados.

## Adendo Desenvolvimento

Atualmente o sistema está em fase de desenvolvimento, sendo assim certas funcionalidades, como a execução de batalhas entre personagens, ainda não estão disponíveis.

## Tecnologias Usadas

O sistema utiliza Python para a criação da lógica interna a partir do desenvolvimento em POO, junto das bibliotecas padrão sqlite3 (para criação e manipulação do banco de dados através de SQL) e enum (para tipagem de dados como tipos de item e habilidade).

## Como executar o projeto

Pré-requisitos: Python 3.10 ou superior instalado (não há dependências externas — o projeto usa apenas bibliotecas padrão do Python).

1. Clone o repositório:

```
git clone https://github.com/arthur-lacerd/sistema-rpg-terminal
```

2. Entre na pasta do projeto:

```
cd sistema-rpg-terminal
```

3. Execute o programa:

```
python src/main.py
```

## Estrutura do projeto

 **data:**
- Banco de dados do projeto

**infra:**
- Lógica de manipulação e criação base do banco de dados

**models:**
- Modelagem das principais entidades do projeto, como personagem, item e atributo

**repositories:**
- Responsável pela lógica por trás da manipulação de dados, dividida de acordo com o que cada repositório manipula

**services:**
- Lógica por trás do sistema de batalhas

**utils:**
- Funções auxiliares para o desenvolvimento do projeto

## Aprendizados

Com o desenvolvimento desse sistema, fui capaz de aprofundar meus conhecimentos em POO, além de aprender sobre estruturação de projetos e modelagem de dados com SQL.
