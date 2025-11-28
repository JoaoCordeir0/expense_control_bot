# Bot de Controle de Gastos no Telegram

Este projeto é um **bot de controle financeiro pessoal**, desenvolvido para o Telegram, que permite registrar gastos, consultar resumos mensais, gerar gráficos e calcular quanto resta do salário.  
O bot utiliza técnicas avançadas de IA, como **Engenharia de Prompt** e **ReAct Prompting**, além de integração com serviços externos (como API de cotação de moedas).

---

## 🚀 Funcionalidades

O bot entende comandos e mensagens naturais para registrar e consultar gastos.  
A seguir, todos os comandos disponíveis:

### **Comandos principais**
| Comando | Função |
|--------|--------|
| **/start** | Inicia uma conversa com o bot |
| **/resumo** | Mostra os gastos do mês atual |
| **/resumo setembro** | Mostra os gastos de um mês específico |
| **/grafico** | Gera um gráfico dos seus gastos |
| **/grafico setembro** | Gera um gráfico de um mês específico |
| **/calcular \<seu-salário>** | Calcula quanto sobrou do salário após os gastos |
| **/suporte** | Envia informações de suporte ao usuário |

---

## 📝 Registro de Gastos

Para registrar um novo gasto, basta enviar uma mensagem neste formato:


### Exemplos:

- `Gastei 44.50 no Mercado`
- `Gastei 250 reais no restaurante em 4 parcelas`

---

## 📊 Exemplos de Uso dos Comandos

- `/resumo`
- `/resumo janeiro`
- `/calcular 5.000 maio`
- `/grafico`
- `/grafico linha maio`
- `/grafico pizza agosto`
- `/grafico barra-vertical abril`

---

## 🧠 Técnicas de Inteligência Artificial Utilizadas

Este projeto foi desenvolvido aplicando conceitos de LLM.
Abaixo estão as técnicas principais.

---

## 🧩 1. Engenharia de Prompt (Prompt Engineering)

A **Engenharia de Prompt** foi utilizada extensivamente para:

- estruturar as intenções do usuário;
- reduzir ambiguidades;
- evitar interpretação incorreta de comandos;
- criar respostas mais naturais e úteis.
- ajudar e tirar dúvidas do usuário.

Alguns exemplos de técnicas aplicadas:

### ✔ *Prompt de Instrução*
O bot foi instruído com prompts estruturados contendo:

- comportamentos esperados,
- regras de interpretação,
- exemplos de entradas e saídas.

### ✔ *Desambiguação por contexto*
Quando o usuário envia apenas “Gastei 40 no lanche”, o bot reconhece:

- valor → 40  
- descrição → “lanche”  
- parcelas → 1 (padrão)

Isso só é possível graças a um prompt construído para interpretar padrões de linguagem natural.

### ✔ *Padronização de respostas*
Todas as respostas seguem:

- linguagem clara,
- concisa,
- adotando sempre o mesmo formato.

---

## 🔄 2. ReAct Prompting (Raciocínio + Ação)

O sistema usa **ReAct Prompting**, uma técnica onde o modelo:

1. **Raciocina** sobre o pedido do usuário,
2. Decide **qual ação realizar** (ferramenta, função ou cálculo),
3. Executa a ação,
4. Retorna o resultado final.

## 🌐 3. Uso de Ferramentas Externas (APIs)

O bot integra ferramentas externas usando a abordagem ReAct, como por exemplo:

### ✔ API de Cotação de Moedas
Um recurso do sistema utiliza:

- consulta de câmbio (ex.: converter gastos em USD para BRL automaticamente).

A IA:

1. detecta que precisa da cotação,  
2. chama a ferramenta externa,  
3. recebe a resposta,  
4. aplica no cálculo final.

---

## 🏗 Arquitetura do Projeto

- **Python** como linguagem de programação
- **Banco de dados SQLite** para armazenar gastos
- **Integração com Telegram Bot API**
- **Camada de IA** para interpretação de linguagem natural
- **Serviços de gráficos** (matplotlib, seaborn ou libs equivalentes)
- **APIs externas** (como cotação de moedas)

---

## 📚 Objetivo do Trabalho

Desenvolver um sistema que:

- utiliza IA de forma prática,
- interpreta linguagem humana,
- toma decisões com ReAct,
- chama ferramentas externas,
- produz valor real para um usuário comum.
- fornece um controle financeiro para os usuários.

## 🛠️ Instruções para executar o projeto:

### 🧩 Criar o arquivo .env

1. Duplique o arquivo de exemplo:
```bash
cp .env.example .env
```
2. Abra o arquivo .env recém-criado.
3. Preencha cada variável com suas informações reais

- ENV → Define o ambiente (development ou production).
- TELEGRAM_BOT_TOKEN → Token do bot fornecido pelo BotFather.
- ADMIN_ID → ID do administrador no Telegram.
- DATABASE_URL → Caminho do banco de dados (SQLite por padrão).
- GEMINI_API_KEY → Chave da API Gemini usada pela IA.

### 🛠️ Rodar o projeto python:
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate # Para Linux
venv/Script/Activate # Para Windows
```
```bash
pip install -r requirements.txt
```
```bash
python main.py
```