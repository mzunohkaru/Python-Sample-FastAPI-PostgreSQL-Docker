# FastAPI Command

$ uvicorn main:app --reload

# Docker Command

$ docker compose up --build
$ docker-compose up
$ docker-compose up -d

## 新しいPythonパッケージを追加した場合
$ docker-compose build --no-cache

## データベース (Postgres) へのアクセス
$ docker-compose exec db psql -U user -d todo

## データベースのマイグレーション
$ docker-compose run app sh -c "cd api && python migrate_db.py"

# 実行結果

- http://0.0.0.0:8000/docs#/
- http://0.0.0.0:8000/redoc

## GETメソッド
curl -X 'GET' 'http://0.0.0.0:8000/tasks' -H 'accept: application/json'

## POSTメソッド
curl -X 'POST' 'http://0.0.0.0:8000/tasks' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"title": "〇〇"}'

## PUTメソッド
curl -X 'PUT' 'http://0.0.0.0:8000/tasks/1' -H 'accept: application/json' -H 'Content-Type: application/json' -d '{"title": "〇〇"}'

## DELETEメソッド
curl -X 'DELETE' 'http://0.0.0.0:8000/tasks/1' -H 'accept: application/json'

## PUTメソッド
curl -X 'PUT' 'http://0.0.0.0:8000/tasks/2/done' -H 'accept: application/json'

## DELETEメソッド
curl -X 'DELETE' 'http://0.0.0.0:8000/tasks/2/done' -H 'accept: application/json'