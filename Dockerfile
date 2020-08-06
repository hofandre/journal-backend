FROM python:3
WORKDIR journal-backend
COPY requirements.txt ./.
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src/.

EXPOSE 5000

WORKDIR src

CMD flask run --host=0.0.0.0
