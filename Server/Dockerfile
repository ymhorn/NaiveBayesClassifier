FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["uvicorn","clientServer:app","--host","0.0.0.0","--port","8080"]