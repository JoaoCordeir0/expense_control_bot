## Bot telegram para controle de gastos

## Comandos para rodar:

```bash
python3 -m venv venv
```
```bash
source venv/bin/activate # Para Linux
venv/Script/Activate # Para Windows
```
```bash
pip install -r requirements.txt
```
```bash
python main.py
```

## Bots

> https://t.me/ControleDeGastosAIDevBot

> https://t.me/ControleDeGastosAIBot


## Banco de dados local

```bash
sudo docker run --name mysql-local -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=bot -p 3306:3306 -d mysql:8
```
```bash
sudo docker exec -it mysql-local mysql -uroot -p
```