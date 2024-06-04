from flask import request, current_app
from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import jwt_required, get_jwt_identity
from http import HTTPStatus
from datetime import datetime, timedelta
from ..models.orders import Order
from ..models.user import User
from ..utils import db
from ..message.message import send_email

orders = Namespace('orders', description="orders namespace")

# for the get function to return as json
order_model = orders.model(
    'Order', {
        'order_id': fields.Integer(description="order number"),
        'client': fields.String(required=True, description="name of client"),
        'order_title': fields.String(required=True, description="title of the order e.g: wedding cake"),
        'description': fields.String(required=True, description="description of the order"),
        'price': fields.Float(required=True, description="negotiated price for the order"),
        'created_at': fields.DateTime(readonly=True, description="date of order entry"),
        'updated_at': fields.DateTime(readonly=True, description="date order got edited"),
        'due_date': fields.Date(required=True,
        description="due date to deliver order"),
        'completed': fields.Boolean(description="oder completion status"),
        'user_id': fields.Integer(required=True)
    }
)

# on what the post function is to expect
place_order_model = orders.model(
    'New_Order', {
        'client': fields.String(required=True, description="name of client"),
        'order_title': fields.String(required=True, description="title of the order e.g: wedding cake"),
        'description': fields.String(required=True, description="Details of the pastry needed by the client"),
        'price': fields.Float(required=True, description="negotiated price for the order"),
        'due_date': fields.Date(required=True, description="due date to deliver order")
    }
)

update_order_model = orders.model(
    'Update_Order', {
        'client': fields.String(required=True, description="name of client"),
        'order_title': fields.String(required=True, description="title of the order e.g: wedding cake"),
        'description': fields.String(required=True, description="Details of the pastry needed by the client"),
        'price': fields.Float(required=True, description="negotiated price for the order"),
        'due_date': fields.Date(required=True, description="due date to deliver order"),
        'completed': fields.Boolean(description="oder completion status")
    }
)

@orders.route('/')
class Orders(Resource):

    # get all user orders
    @orders.marshal_with(order_model)
    @orders.doc(
        description="Retrieves all orders of an authorized user"
    )
    @jwt_required()
    def get(self):
        """
        Displays all orders of a particular user only
        """
        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        if not current_user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND

        orders = Order.query.filter_by(user=current_user).all()

        return orders, HTTPStatus.OK

    # post a new order
    @orders.expect(place_order_model)
    @orders.marshal_with(order_model)
    @orders.doc(
        description="Input new order for an authorized user"
    )
    @jwt_required()
    def post(self):
        """
        Creates a new order for an authorized user
        """
        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        if current_user:
            data = orders.payload

            due_date = datetime.strptime(data.get('due_date'), '%Y-%m-%d').date()

            max_order_id = Order.query.filter_by(user_id=current_user.id).order_by(Order.order_id.desc()).first()
            new_order_id = 1 if max_order_id is None else max_order_id.order_id + 1

            new_order = Order(
                order_id=new_order_id,
                client=data.get('client'),
                order_title=data.get('order_title'),
                description=data.get('description'),
                price=data.get('price'),
                due_date=due_date,
                user_id = current_user.id
            )

            new_order.save()

            msg = f"You have set a new order titled({new_order.order_title}), for client({new_order.client}), to be delivered on or before ({new_order.due_date})"

            send_email('Bakers-kiss Order Creation', msg, current_user.email)

            return new_order, HTTPStatus.CREATED

        return {'message': 'order not created'}, HTTPStatus.UNAUTHORIZED


@orders.route('/<int:order_id>')
class OneOrder(Resource):
    # get a particular order
    @orders.marshal_with(order_model)
    @orders.doc(
        description="Retrieve an order of an authorized user by its id",
        params={
            "order_id":"id of order to retrieve"
        }
    )
    @jwt_required()
    def get(self, order_id):
        """
        Displays a particular order of an authorized user
        Args:
            order_id(int): id to get specific order
        """
        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        if not current_user:
            return {'message': 'User not found'}, HTTPStatus.NOT_FOUND
        
        order = Order.query.filter_by(user=current_user, order_id=order_id).first()

        return order, HTTPStatus.OK

    # update a particular order
    @orders.expect(update_order_model)
    @orders.marshal_with(order_model)
    @orders.doc(
        description="Updates an order of an authorized user by its id",
        params={
            "order_id": "id of order to update"
        }
    )
    @jwt_required()
    def put(self, order_id):
        """
        Updates a particular order of an authorized user
        Args:
            order_id(int): id to get specific order to update
        """
        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        update_order = Order.query.filter_by(user=current_user, order_id=order_id).first()

        if not update_order:
            return {"message": "Order Not Found"}, HTTPStatus.NOT_FOUND

        data = orders.payload

        if 'client' in data:
            update_order.client = data['client']
        if 'order_title' in data:
            update_order.order_title = data['order_title']
        if 'description' in data:
            update_order.description = data['description']
        if 'price' in data:
            update_order.price = data['price']
        if 'due_date' in data:
            update_order.due_date = datetime.strptime(data.get('due_date'), '%Y-%m-%d').date()
        if 'completed' in data:
            update_order.completed = data['completed']
            # send message on completion
            if update_order.completed:
                msg = f"Congratulations, you completed order with title ({update_order.order_title}) from client ({update_order.client})"
                email = current_user.email

                send_email('Bakers-kiss', msg, email)
        db.session.commit()

        return update_order, HTTPStatus.OK

    # delete a particular order
    @orders.marshal_with(order_model)
    @orders.doc(
        description="Deletes an order of an authorized user by its id",
        params={
            "order_id": "id of order to delete"
        }
    )
    @jwt_required()
    def delete(self, order_id):
        """
        Deletes a particular order of an authorized user
        Args:
            order_id(int): id to get specific order to delete
        """
        username = get_jwt_identity()

        current_user = User.query.filter_by(username=username).first()

        order = Order.query.filter_by(user=current_user, order_id=order_id).first()
        
        if order:
            msg = f"You deleted an order for client({order.client}), with order title({order.order_title})"

            send_email("Bakers-Kiss Order Deletion", msg, current_user.email)
            order.delete()

            return order, HTTPStatus.NO_CONTENT
        
        return {'message': 'Order Not Found'}, HTTPStatus.NOT_FOUND