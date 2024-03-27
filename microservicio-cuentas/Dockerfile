FROM sanicframework/sanic:3.8-latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "main.py"]