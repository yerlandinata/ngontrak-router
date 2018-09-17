from flask import Flask, json, request, Response
from driver import get_driver
from client_list import get_client_list
from block_client import get_blocked_clients, block_client_by_mac, unblock_all

app = Flask(__name__)
driver = get_driver(headless=True)

@app.errorhandler(404)
def page_not_found(e):
    return Response(status=404, mimetype='application/json')

@app.errorhandler(500)
def page_server_error(e):
    return Response(status=404, mimetype='application/json')

@app.route('/api/clients', methods = ['GET'])
def clients():
    return app.response_class(
        response=json.dumps([{
            'mac_address': mac,
            'ip_address': ip
        } for mac, ip in get_client_list(driver)]),
        mimetype='application/json'
    )

@app.route('/api/black-list', methods = ['GET', 'POST', 'DELETE'])
def blocked():
    if request.method == 'GET':
        return app.response_class(
            response=json.dumps([{
                'mac_address': mac,
            } for mac in get_blocked_clients(driver)]),
            mimetype='application/json'
        )
    elif request.method == 'POST':
        payload = request.get_json()
        if 'mac' not in payload.keys():
            return Response(status=400, mimetype='application/json')
        block_client_by_mac(driver, payload['mac'])
        return Response(status=201, mimetype='application/json')
    elif request.method == 'DELETE':
        unblock_all(driver)
        return Response(status=201, mimetype='application/json')
