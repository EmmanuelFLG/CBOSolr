# extrator.py
import pandas as pd
from helpers.application import app
from helpers.database.database import db
from helpers.database.solr import solr
from models.CBOModel import CBOEntidade

CSV_FILE = "cbo2002-ocupacao.csv"  # Caminho do seu CSV

def extrair_dados(csv_file):
    try:
        print("Iniciando importação...")

        # Lê CSV
        df = pd.read_csv(csv_file, sep=";", encoding="ISO-8859-1")

        with app.app_context():  # necessário para usar db.session
            for row in df.itertuples():
                # Cria entidade
                entidade = CBOEntidade(
                    codigo=int(row.CODIGO),
                    titulo=str(row.TITULO)
                )

                # Adiciona ao banco
                db.session.add(entidade)
                db.session.flush()  # necessário para obter o ID

                # Adiciona ao Solr
                solr.add([{
                    "id": str(entidade.id),
                    "codigo": entidade.codigo,
                    "titulo": entidade.titulo
                }], commit=True)  # commit garante que fique visível no Solr

            # Comita tudo no PostgreSQL
            db.session.commit()
            print("Importação concluída com sucesso!")

    except Exception as e:
        db.session.rollback()
        print(f"Erro durante a importação: {e}")

if __name__ == "__main__":
    extrair_dados(CSV_FILE)
