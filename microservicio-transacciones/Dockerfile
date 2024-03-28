FROM python:3.9

WORKDIR /app

COPY . .

RUN python -m pip install -r requirements.txt

EXPOSE 8001

CMD ["python", "main.py"]