import pandas as pd
import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Baixar recursos do NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Função para carregar listas a partir de arquivos .txt
def carregar_lista(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        return [linha.strip().lower() for linha in f if linha.strip()]

# Carregar listas externas
expressoes_positivas = carregar_lista("expressoes_positivas.txt")
expressoes_negativas = carregar_lista("expressoes_negativas.txt")
palavras_positivas = carregar_lista("palavras_positivas.txt")
palavras_negativas = carregar_lista("palavras_negativas.txt")

# Stopwords
stop_words = set(stopwords.words('portuguese'))

# Pré-processamento
def preprocess(texto):
    texto = texto.lower()
    tokens = word_tokenize(texto)
    tokens = [t for t in tokens if t not in stop_words and t not in string.punctuation]
    return tokens

# Classificação com regras e checagem de negação
def classificar_regras(texto):
    texto_lower = texto.lower()

    # Verificar expressões compostas primeiro
    if any(exp in texto_lower for exp in expressoes_positivas):
        return 'positiva'
    if any(exp in texto_lower for exp in expressoes_negativas):
        return 'negativa'

    tokens = preprocess(texto)
    positivas = 0
    negativas = 0

    for i, palavra in enumerate(tokens):
        if palavra in palavras_positivas:
            if i > 0 and tokens[i - 1] == 'não':
                negativas += 1
            else:
                positivas += 1
        elif palavra in palavras_negativas:
            negativas += 1

    if positivas > negativas:
        return 'positiva'
    elif negativas > positivas:
        return 'negativa'
    return 'neutra'

# Carregar base de dados
df = pd.read_csv('reviews_smartphone.csv', encoding='latin-1', sep=';')
df.dropna(inplace=True)

# Classificar automaticamente
df['Sentimento'] = df['Reviews'].apply(classificar_regras)

# Exibir amostra
print("\n📊 Amostra classificada:")
print(df[['Reviews', 'Sentimento']].sample(5))

# Entrada interativa
while True:
    entrada = input("\nDigite uma frase para analisar (ou 'sair' para encerrar): ")
    if entrada.lower() == 'sair':
        break
    sentimento = classificar_regras(entrada)
    print("🔎 Sentimento previsto:", sentimento)
