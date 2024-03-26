from sanic import Sanic
from sanic.response import text

app = Sanic("transactions")

@app.get("/")
async def hello_world(request):
    return text("Hello, transactions.")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8081, debug=True)