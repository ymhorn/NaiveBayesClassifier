FROM python:latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn","modelServer:app","--host","0.0.0.0","--port","8000"]