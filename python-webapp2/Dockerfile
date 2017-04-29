FROM python:3.4

RUN pip install Flask==0.10.1 redis==2.10.3

WORKDIR /app
COPY app /app
EXPOSE 5000

CMD ["python", "main.py"]
