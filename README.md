# CBOSolr 


na raiz do projeto:

```docker compose up --build```


**Terminal:**
1. Iniciar container flask
```docker exec -it flask_api sh``` 

2. Inicializar o ambiente de migração do banco de dados
```flask db init ```

4. Executar o migrate
```flask db migrate```

6. Aplicar as migrações pendentes
```flask db upgrade```

7. Executar o extrator
```python -m extrator.CBOExtrator```

8. Entrar no container do postgres
```docker compose exec postgres psql -U postgres -d cbodb```

9. Consultar a tabela
```select * from "tb_CBOEntidade";```


**Fora dos containers testar os endpoints:**

```GET http://localhost:5000/CBOEntidades/buscar?q=Analista```

curl http://localhost:5000/CBOEntidades/1
