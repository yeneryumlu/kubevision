'''Metrics'''

from flask_restx import Namespace, Resource
from flask import jsonify, request
from dao.metricsdao import MetricsDAO

ns = Namespace('metrics', description='Metrics operations')
dao = MetricsDAO()

@ns.route('/add')
class Metrics(Resource):
    '''Metrics insert'''
    @ns.doc('add new metrics')
    def post(self):
        '''add new metrics'''
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            print(json)
            [code, message] = dao.create(cluster_name=json["name"], version_info=json["version_info"], nodes=json["nodes"], namespaces=json["namespaces"])
            return { "message" : message }, code
        else:
            return 'Content-Type not supported!'
