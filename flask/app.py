# from flask import Flask
# from flask_restful import reqparse, abort, Api, Resource

# app = Flask(__name__)
# api = Api(app)

# ITEMS = {
#     'item1': {'name': 'Allen', 'age': 19},
#     'item2': {'name': 'Lily', 'age': 18},
#     'item3': {'name': 'James', 'age': 20},
# }

# parser = reqparse.RequestParser()
# parser.add_argument('name', type=str, required=True, help='need name data')
# parser.add_argument('age', type=int, required=True, help='need age data')


# class Todo(Resource):
#     def put(self, item_id):
#         args = parser.parse_args()
#         item = {'name': args['name'], 'age': args['age']}
#         ITEMS[item_id] = item
#         return item, 201

#     def get(self, item_id):
#         # abort_if_item_doesnt_exist(item_id)
#         return ITEMS[item_id], 200

#     def delete(self, item_id):
#         # abort_if_item_doesnt_exist(item_id)
#         del ITEMS[item_id]
#         return '', 204


# # 操作（post / get）资源列表
# class TodoList(Resource):
#     def get(self):
#         return ITEMS, 200

#     def post(self):
#         args = parser.parse_args()
#         item_id = 1
#         ITEMS[item_id] = {'name': args['name'], 'age': args['age']}
#         return ITEMS[item_id], 201


# # 设置路由
# api.add_resource(TodoList, '/items')
# api.add_resource(Todo, '/items/<item_id>')

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

ITEMS = {
    'item1': {'name': 'Allen', 'age': 19},
    'item2': {'name': 'Lily', 'age': 18},
    'item3': {'name': 'James', 'age': 20},
}

class Todo(Resource):
    def put(self, item_id):
        item = {'name': '123', 'age': 456}
        return item, 201

    def get(self, item_id):
        item = {'name': '123', 'age': 456}
        return item, 200

    def delete(self, item_id):
        del ITEMS[item_id]
        return '', 204


api.add_resource(Todo, '/items/<item_id>')

if __name__ == '__main__':
    app.run()
