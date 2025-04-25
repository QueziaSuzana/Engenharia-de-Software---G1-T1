# 🌐 Sistema de Consulta de Oportunidades de Gênero em Empresas

Este projeto tem como objetivo promover a transparência e acessibilidade a dados sobre **representatividade de gênero dentro de empresas**, alinhado ao Objetivo de Desenvolvimento Sustentável (ODS) 5 da ONU: **Igualdade de Gênero**.

## 📌 Visão Geral

A solução foi implementada como uma aplicação web simples, composta por:

- **Frontend (Website):** Um site desenvolvido em HTML, CSS e JavaScript, com um formulário que permite ao usuário consultar dados sobre empresas e seus setores.
- **Backend (API):** Desenvolvido em FastAPI, o backend se conecta a um banco SQLite local para realizar consultas e gerar relatórios.
- **Banco de Dados:** SQLite local contendo os dados de empresas, setores, funcionários, taxas e idades médias.
- **Relatórios:** A API é capaz de gerar arquivos PDF com estatísticas por empresa e setor.

## 🚀 Funcionalidades

- Consultar uma empresa e visualizar a taxa de gênero por setor.
- Gerar um relatório completo (PDF) com a distribuição de gênero, idade média e totais por setor.
- Interface simples e intuitiva, acessível via navegador.

## 🧱 Tecnologias Utilizadas

| Camada         | Tecnologia         |
|----------------|--------------------|
| Frontend       | HTML, CSS, JavaScript (Fetch API) |
| Backend / API  | Python + FastAPI   |
| Banco de Dados | SQLite             |
| Relatórios     | Report Generator em Python (PDF) |

## 🗂 Estrutura do Projeto

 raiz-do-repositorio/ ├── API/ # Backend em FastAPI ├── Website/ # Frontend com HTML/CSS/JS ├── Videos/ # Vídeo demonstrativo │ └── demo-tp3.mp4 ├── docs/ # Documentação do projeto │ ├── arquitetura.md │ └── c4-container.drawio ├── report-exemplo.pdf # Exemplo de relatório gerado ├── README.md # └── requirements.txt 
