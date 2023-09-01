'''Clusters'''

from flask_restx import Namespace, Resource
from flask import jsonify, request
import json

from requests import get
from dao.k8sdao import K8sDAO
from entity.entities import ClusterEntityEncoder

ns = Namespace('cluster', description='Cluster operations')
dao = K8sDAO()

@ns.route('/')
class Clusters(Resource):
    '''Cluster list'''
    @ns.doc('get_clusters')
    def get(self):
        '''All Clusters result'''
        result = dao.get_all()
        # return jsonify(result)
        return json.loads(json.dumps(result, indent=4, cls=ClusterEntityEncoder))

@ns.route('/detail/<name>')
class Cluster(Resource):
    '''Cluster detail'''
    @ns.doc('get_cluster_detail')
    def get(self, name):
        '''Cluster Detail result'''
        result = dao.get_cluster_detail(name)
        return result, 200


@ns.route('/add')
class AddCluster(Resource):
    '''Add new cluster'''
    @ns.doc("add new cluster to system")
    def post(self):
        """Adds a cluster to watch"""
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json = request.json
            [status, obj] = dao.create(json["name"], json["environment"], json["apiserver"], json["token"])
            if(status):
                return json, 201
            else:
                return { "message" : obj }, 400
        else:
            return 'Content-Type not supported!'


