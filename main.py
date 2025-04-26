import pandas as pd
import flask
import kagglehub
from kagglehub import KaggleDatasetAdapter
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

class MachineLearning(object):
    def __init__(self):
        self.arvore = None

    def training(self):
        try:
            file_path = "email_phishing_data.csv"
            df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            "ethancratchley/email-phishing-dataset",
            file_path,)

            classe_0 = df[df['label'] == 0].sample(n=6949, random_state=42)
            classe_1 = df[df['label'] == 1]

            df = pd.concat([classe_0, classe_1]).sample(frac=1, random_state=42).reset_index(drop=True)

            target = df['label']
            features = df.drop(['label'], axis=1)

            X_train, X_test, Y_train, Y_test = train_test_split(features, target, test_size=0.2, random_state=13)

            arvore = DecisionTreeClassifier(max_depth=10)

            self.arvore = arvore.fit(X_train, Y_train)
            return True
        except Exception as e:
            return False, str(e)


    def pred(self,data):
        if self.arvore is None:
            raise ValueError("Model not trained")
        return self.arvore.predict(data).tolist()

app = flask.Flask(__name__)

machine = MachineLearning()

@app.route('/train', methods=['POST'])
def train():
    if machine.training():
        resposta = {
            'Resultado': 'Training completed.'
        }
        return flask.jsonify(resposta), 200
    else:
        resposta = {
            'Resultado': 'Training not done.'
        }
        return flask.jsonify(resposta), 500

@app.route('/pred', methods=['POST'])
def pred():
    #num_words
    #num_unique_words
    #num_stopwords
    #num_links
    #num_unique_domains
    #num_email_adresses
    #num_spelling_errors
    #num_urgent_keywords

    data = flask.request.get_json()

    dataDf = pd.DataFrame([data])

    resultado = machine.pred(dataDf)
    return flask.jsonify({"prediction": resultado[0]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)