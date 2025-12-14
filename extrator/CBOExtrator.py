import pandas as pd
from helpers.database import db
from helpers.solr import solr
from models.CBOModel import CBOEntidade

def extrairDados(csv_file):
    try:
        print("Iniciando importação...")

        df = pd.read_csv(csv_file, sep=";", encoding="ISO-8859-1")

        for row in df.itertuples():
            entidade = CBOEntidade(
                codigo=int(row.CODIGO),
                titulo=str(row.TITULO)
            )

            db.session.add(entidade)
            db.session.flush()  

            
            solr.add([{
                "id": str(entidade.id),
                "codigo": entidade.codigo,
                "titulo": entidade.titulo
            }])

        db.session.commit()
        print("Importação concluída com sucesso!")

    except Exception as e:
        db.session.rollback()
        print(f"Erro durante a importação: {e}")

extrairDados("cbo2002-ocupacao.csv")
