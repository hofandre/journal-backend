docker build -t journalserver .
docker run -d  --env-file .env-list -p 5000:5000 journalserver:latest