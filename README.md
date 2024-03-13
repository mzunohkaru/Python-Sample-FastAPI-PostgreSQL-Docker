# FastAPI Command

$ uvicorn main:app --reload

# Docker Command

$ docker compose up --build
$ docker-compose up
$ docker-compose up -d

## 新しいPythonパッケージを追加した場合
$ docker-compose build --no-cache

## データベース (MySQL) へのアクセス
$ docker-compose exec db mysql -uuser -ppassword todo

## データベースのマイグレーション
$ docker-compose run app sh -c "cd api && python migrate_db.py"


http://0.0.0.0:8000