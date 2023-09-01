'''Healthcheck'''

from flask_restx import Namespace, Resource

ns = Namespace('health', description='Healthcheck operations')


@ns.route('/')
class HealthCheck(Resource):
    '''Healthcheck'''
    @ns.doc('get_healthcheck')
    def get(self):
        '''Healthcheck result'''
        return 'Sirius Api is Up!'
