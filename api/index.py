from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/produtos")
def get_produtos():
    return {"message": "Hello World"}

@app.post("/cadastrarProduto")
def post_produto():
    return {"message": "produto cadastrado"} 

@app.patch("/editarProduto/{produtoId}")
def update_produto():
    return {"message": "produto atualizado"} 

@app.delete("/removerProduto/{produtoId}")
def delete_produto():
    return {"message": "produto removido"} 

@app.get("/lerPedidos/{usuarioId}")
def read_pedido():
    return {"message": "lista de pedidos"}

@app.post("/cadastrarUsuario")
def post_produto():
    return {"message": "usuário cadastrado"} 

@app.patch("/editarUsuario/{usuarioId}")
def update_produto():
    return {"message": "usuario atualizado"} 

@app.delete("/removerUsuario/{usuarioId}")
def update_produto():
    return {"message": "usuario removido"} 
