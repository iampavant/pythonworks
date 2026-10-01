from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)
products = {101:{"name":"Product 101"}}
class Product(Resource):
    def get(self, pid):
        return products.get(pid, {"message": "Not found"})
    def post(self, pid):
        products[pid] = {"name": f"Product {pid}"}
        return {"message": "Created", "data": products[pid]}
api.add_resource(Product, "/product/<int:pid>")
if __name__ == "__main__":
    app.run(debug=True)
