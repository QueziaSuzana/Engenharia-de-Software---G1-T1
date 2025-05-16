# ✅ Plano de Testes da Aplicação

Este documento descreve os testes realizados na aplicação desenvolvida para consulta de oportunidades de gênero em empresas. Os testes têm como objetivo garantir que os principais fluxos funcionem corretamente, validando tanto o frontend quanto o backend da aplicação.

---

## 🧪 1. Testes Funcionais

### 1.1 Consulta de empresa via formulário

| Caso de Teste                          | Resultado Esperado                                     | Resultado Obtido | Status |
|----------------------------------------|--------------------------------------------------------|------------------|--------|
| Preencher o nome de uma empresa válida e clicar em “Consultar” | Dados da empresa e setores são exibidos corretamente   | ✅ Dados exibidos | Passou |
| Inserir nome de empresa inexistente    | Mensagem de erro ou retorno vazio                      | ✅ Mensagem exibida | Passou |
| Submeter sem preencher o campo         | Alerta ou validação evitando envio                     | ✅ Formulário impede envio | Passou |

---

### 1.2 Geração de relatório PDF

| Caso de Teste                          | Resultado Esperado                                     | Resultado Obtido | Status |
|----------------------------------------|--------------------------------------------------------|------------------|--------|
| Gerar relatório de empresa com setores | Arquivo PDF com dados por setor                        | ✅ PDF gerado com dados | Passou |
| Gerar relatório com nome de empresa inexistente | PDF vazio ou erro controlado                          | ✅ PDF vazio retornado | Passou |

---

### 1.3 Requisições à API

| Endpoint                      | Método | Entrada               | Esperado                       | Resultado Obtido | Status |
|------------------------------|--------|------------------------|--------------------------------|------------------|--------|
| `/consulta/{empresa}`        | GET    | Nome válido de empresa | Dados JSON dos setores         | ✅ JSON retornado | Passou |
| `/relatorio/{empresa}`       | GET    | Nome válido de empresa | PDF de relatório gerado        | ✅ PDF retornado | Passou |

---

## 🧩 2. Testes de Integração Frontend ↔️ API

| Ação do Usuário                               | Comportamento Esperado                         | Resultado Obtido | Status |
|------------------------------------------------|------------------------------------------------|------------------|--------|
| Consulta pelo site com empresa válida          | Frontend envia requisição e exibe dados        | ✅ Dados exibidos | Passou |
| Clique no botão de gerar relatório             | PDF é baixado ou aberto                        | ✅ PDF gerado e salvo | Passou |

---

## 🧰 3. Testes Técnicos (manuais)

| Item Verificado                    | Método de Teste                                  | Resultado |
|-----------------------------------|--------------------------------------------------|-----------|
| Conexão com banco SQLite          | Teste de leitura de dados                        | ✅ Ok     |
| Tempo de resposta da API          | Inspecionar via browser e terminal               | ✅ Ok |
| Funcionamento do PDFKit + wkhtmltopdf | Teste local de geração de arquivo                | ✅ Ok     |



