'''Nodes'''

from flask_restx import Namespace, Resource
from flask import jsonify
from dao.k8sdao import K8sDAO

ns = Namespace('namespace', description='Namespace operations')
dao = K8sDAO()

@ns.route('/')
class Namespace(Resource):
    '''Namespace list'''
    @ns.doc('get_namespace')
    def get(self):
        '''All Namespace result'''
        result = dao.get_all_namespaces()
        return jsonify(result)
        


