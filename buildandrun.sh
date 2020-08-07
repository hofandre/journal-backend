docker build -t journalserver .
docker run -d -p --env-file .env-list 5000:5000 journalserver:latest