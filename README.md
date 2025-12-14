# CBOSolr 


na raiz do projeto:

docker compose up --build


Terminal:
docker exec -it flask_api sh ----- iniciar container flask

flask db init 

flask db migrate ------- executar o migrate

flask db upgrade

python -m extrator.CBOExtrator ------ executar o extrator

docker compose exec postgres psql -U postgres -d cbodb --------- entrar no container do postgres

select * from "tb_CBOEntidade"; ------ consultar a tabela


fora dos containers testar os endpoints:

GET http://localhost:5000/CBOEntidades/buscar?q=Analista

curl http://localhost:5000/CBOEntidades/1
