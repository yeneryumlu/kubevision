'''Metrics'''

from flask_restx import Namespace, Resource
from flask import jsonify, request
from dao.metricsdao import MetricsDAO

ns = Namespace('clustermetrics', description='ClusterMetrics operations')
dao = MetricsDAO()

@ns.route('/')
class ClusterMetrics(Resource):
    '''Cluster Metrics retrieval'''
    @ns.doc('get cluster metrics')
    def get(self):
        '''get cluster metrics'''
        result = dao.get_cluster_metrics()
        return result