
# 👥 Integrantes#

- Alan de Souza Maximiano - RM557088@fiap.com.br
- Lancelot Chagas Rodrigues - RM554707@fiap.com.br
- Marcia Ricardo Rosano - RM557464@fiap.com.br
- Mizael Vieira Bezerra - RM555796@fiap.com.br
- Paulo Carvalo Ruiz Borba - RM554562@fiap.com.br

## 🔍 **Classificador de Sentimentos para Avaliações de Smartphones**

Este projeto desenvolve um classificador de sentimentos em português para detectar se avaliações de smartphones expressam sentimento positivo, negativo ou neutro. Utilizamos técnicas de Processamento de Linguagem Natural (NLP) com o NLTK, além de uma base de regras e expressões adaptadas da linguagem natural brasileira.

## **🎯 Objetivo**

Criar uma solução leve e funcional que interprete o sentimento de avaliações escritas, sem uso de modelos de IA pesados, apenas com:

- Expressões e palavras positivas/negativas
- Regras simples de negação
- Interface interativa via terminal

## **🛠️ Como funciona**

- Frases de usuários são pré-processadas (tokenizadas e tratadas)
- O algoritmo compara com listas externas de palavras e expressões positivas/negativas
- Caso detecte negação (“não bom”), isso é tratado como sentimento negativo
- O resultado final é impresso como: positiva, negativa ou neutra

## **📦 Estrutura do projeto**

- classificador_sentimentos.py           # Script principal
- reviews_smartphone.csv                 # Base de dados com avaliações
- expressoes_positivas.txt               # Expressões positivas
- expressoes_negativas.txt               # Expressões negativas
- palavras_positivas.txt                 # Palavras positivas
- palavras_negativas.txt                 # Palavras negativas
- README.md                              # Documentação

## **▶️ Como executar**

### 1. Clone este repositório:

git clone https://github.com/mizaelvieira1/CP1_NLP.git
cd CP1_NLP

### 2. Instale as dependências:

pip install -r requirements.txt

### 4. Garanta que os arquivos .txt estejam no mesmo diretório do script:

- expressoes_positivas.txt
- expressoes_negativas.txt
- palavras_positivas.txt
- palavras_negativas.txt
- reviews_smartphone.csv

### 5. python classificador_sentimentos.py

python classificador_sentimentos.py

### 6. Digite frases no terminal:

Digite uma frase para analisar (ou 'sair' para encerrar): a bateria durou o dia inteiro
🔎 Sentimento previsto: positiva


