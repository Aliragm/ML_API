# ML_API

Uma API simples de Machine Learning para estudo e demonstração.

## Descrição

Este projeto implementa uma API REST básica usando Flask para treinar e realizar predições com um modelo de Machine Learning (Decision Tree). O dataset utilizado é o "Email Phishing Dataset" disponível no Kaggle. A API possui dois endpoints:

- **`/train`** (POST): realiza o treinamento do modelo.
- **`/pred`** (POST): recebe features de um email e retorna se é phishing ou não.

## Funcionalidades

- Carregamento automático do dataset do Kaggle via **kagglehub**.
- Pré-processamento simples e balanceamento das classes.
- Treinamento de um **Decision Tree Classifier** com profundidade máxima de 10.
- Endpoints REST para treinamento e predição.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Aliragm/ML_API.git
   cd ML_API
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
## Uso

### Iniciar a API

Execute o servidor Flask:

```bash
python main.py
```

A API estará disponível em `http://0.0.0.0:5000/`.

### Endpoint `/train`

Realiza o treinamento do modelo. Deve ser chamado via POST:

```bash
curl -X POST http://localhost:5000/train
```

Resposta de sucesso (HTTP 200):

```json
{
  "Resultado": "Training completed."
}
```

### Endpoint `/pred`

Realiza predição usando o modelo treinado. Recebe um JSON com as seguintes features:

- `num_words`: número de palavras no email
- `num_unique_words`: número de palavras únicas
- `num_stopwords`: número de stopwords
- `num_links`: número de links
- `num_unique_domains`: quantidade de domínios distintos
- `num_email_adresses`: número de endereços de email
- `num_spelling_errors`: número de erros ortográficos
- `num_urgent_keywords`: número de palavras urgentes (ex.: "important", "urgent")

Exemplo de requisição:

```bash
curl -X POST http://localhost:5000/pred \
  -H "Content-Type: application/json" \
  -d '{
    "num_words": 100,
    "num_unique_words": 80,
    "num_stopwords": 20,
    "num_links": 2,
    "num_unique_domains": 2,
    "num_email_adresses": 1,
    "num_spelling_errors": 3,
    "num_urgent_keywords": 1
  }'
```

Resposta de exemplo (HTTP 200):

```json
{
  "prediction": 0
}
```

Onde `0` indica email legítimo e `1` phishing.

## Estrutura do Projeto

```
ML_API/
├── main.py            # Código principal da API
├── requirements.txt   # Dependências do projeto
```
## Licença

Este projeto não possui uma licença especificada. Utilize por sua conta e risco.

