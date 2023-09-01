'''Nodes'''

from flask_restx import Namespace, Resource
from flask import jsonify, request
import json
from requests import get
from dao.k8sdao import K8sDAO
from entity.entities import ClusterEntityEncoder

ns = Namespace('node', description='Node operations')
dao = K8sDAO()

@ns.route('/')
class Nodes(Resource):
    '''Cluster list'''
    @ns.doc('get_nodes')
    def get(self):
        '''All Nodes result'''
        result = dao.get_all_nodes()
        return jsonify(result)
        # return json.loads(json.dumps(result, indent=4, cls=ClusterEntityEncoder))

# @ns.route('/detail/<name>')
# class Cluster(Resource):
#     '''Cluster detail'''
#     @ns.doc('get_cluster_detail')
#     def get(self, name):
#         '''Cluster Detail result'''
#         result = dao.get_cluster_detail(name)
#         return result, 200

