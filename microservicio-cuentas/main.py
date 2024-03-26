from sanic import Sanic
from sanic.response import text

app = Sanic("accounts")

@app.get("/")
async def hello_world(request):
    return text("Hello, accounts.")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)