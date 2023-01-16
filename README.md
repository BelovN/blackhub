# Blackhub
Simple proxy server to https://blackrussia.online/

# How to Docker

### Build docker image
```bash
docker build . -t blackhub
```

### Run app
```bash
docker run -p 8000:8000 -v /home/path/to/logs:/app/logs -d blackhub
```

# How to native

### Install requirements
```bash
python3 -m venv venv
. venb bin activate
pip install -r requirements.txt
```

### Run app
```bash
./manage.py runserver
```

### Run Tests
```bash
pytest
```