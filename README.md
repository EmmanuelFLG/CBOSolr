# CBOSolr 


na raiz do projeto:

```docker compose up --build```


**Terminal:**
1. iniciar container flask
```docker exec -it flask_api sh``` 

2. inicializar o ambiente de migração do banco de dados
```flask db init ```

4. executar o migrate
```flask db migrate```

6. aplicar as migrações pendentes
```flask db upgrade```

python -m extrator.CBOExtrator ------ executar o extrator

docker compose exec postgres psql -U postgres -d cbodb --------- entrar no container do postgres

select * from "tb_CBOEntidade"; ------ consultar a tabela


fora dos containers testar os endpoints:

GET http://localhost:5000/CBOEntidades/buscar?q=Analista

curl http://localhost:5000/CBOEntidades/1
