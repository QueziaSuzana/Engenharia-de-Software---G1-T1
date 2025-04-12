# Documentação da Arquitetura do Projeto

## 1. Escolhas de Tecnologias

O projeto foi desenvolvido utilizando tecnologias modernas, leves e de fácil integração, visando simplicidade e funcionalidade:

| Camada         | Tecnologia         | Justificativa |
|----------------|--------------------|----------------|
| Frontend       | HTML, CSS e JavaScript | Simples, leve, e fácil de integrar com a API. Utiliza `fetch` para consumir os endpoints da API. |
| Backend / API  | FastAPI (Python)   | Framework moderno, assíncrono, com excelente performance e tipagem robusta. Ideal para construção de APIs REST. |
| Banco de Dados | SQLite             | Banco leve e embutido, ideal para projetos menores e protótipos. Não exige instalação de servidor. |
| Geração de Relatórios | ReportLab / fpdf / outro método PDF em Python | Permite transformar os dados em relatórios PDF de maneira simples e automatizada. |

---

## 2. Projeto Arquitetural (Modelo C4 - Nível 2: Container)

A arquitetura do sistema foi representada por meio do **C4 Model**, no nível de **Containers**, pois este nível permite detalhar os principais blocos do sistema (Frontend, Backend, Banco de Dados e Gerador de Relatórios) e as relações entre eles.

### 🔗 Visão Geral

- **Usuário** acessa o sistema via navegador.
- **Frontend Web** envia requisições via `fetch` para a **API**.
- **API (FastAPI)** processa os dados, consulta o **banco SQLite** e retorna as informações.
- A API também é responsável por chamar o **módulo gerador de relatórios** que gera um documento PDF estruturado com as informações da empresa consultada.

### Diagrama de Container (C4)

> ![diagrama](docs/c4-container.drawio.png)


---

## 3. Justificativa do Modelo Escolhido (C4)

O **C4 Model** foi escolhido por ser uma abordagem moderna, simples e progressiva para modelagem arquitetural de sistemas de software. Sua divisão em níveis permite visualizar o sistema de maneira hierárquica e compreensível.

- **Nível 1 (Contexto)**: Poderia ser utilizado para mostrar o sistema em seu ecossistema (usuários, outras APIs, etc.), mas foi omitido por simplicidade.
- **Nível 2 (Containers)**: Ideal para o tamanho do projeto, permitindo apresentar as camadas da aplicação com clareza.
- **Nível 3 (Componentes)**: Pode ser explorado futuramente para detalhar a API internamente (rotas, serviços, PDF generator), mas não é obrigatório nesta fase.

---


## Considerações Finais

A arquitetura adotada é simples, modular e adequada ao escopo do projeto. O uso de tecnologias leves facilita o desenvolvimento, manutenção e escalabilidade futura do sistema.



