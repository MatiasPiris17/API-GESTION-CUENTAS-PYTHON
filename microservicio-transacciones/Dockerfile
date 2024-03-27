FROM sanicframework/sanic:3.8-latest

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "main.py"]