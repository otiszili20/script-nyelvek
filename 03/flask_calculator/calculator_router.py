from flask import request, Blueprint
import calculator

calculator_api = Blueprint('calculator',__name__)


@calculator_api.route('/add')
def add_end_point():
    a = float(request.args['a'])
    b = float(request.args['b'])

    return str(calculator.add(a, b))


@calculator_api.route('/sub')
def sub_end_point():
    a = float(request.args['a'])
    b = float(request.args['b'])
    return str(calculator.sub(a, b))


@calculator_api.route('/mul')
def mul_end_point():
    a = request.args['a']
    b = request.args['b']
    return calculator.mul(a, b)


@calculator_api.route('/div')
def div_end_point():
    a = request.args['a']
    b = request.args['b']
    return calculator.div(a, b)
