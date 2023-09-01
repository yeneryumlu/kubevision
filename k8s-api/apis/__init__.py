""" Init """

import flask.scaffold
flask.helpers._endpoint_from_view_func = flask.scaffold._endpoint_from_view_func
from flask_restx import Api
from .healthcheck_ns import ns as healthcheckns
from .cluster_ns import ns as clusterns
from .node_ns import ns as nodens
from .namespace_ns import ns as namespacens
from .metrics_ns import ns as metricsns
from .cluster_metrics_ns import ns as clustermetricsns


api = Api(
    title='KubeVision Api',
    version='1.0',
    description='Kubernetes visibility apis',
)

api.add_namespace(healthcheckns)
api.add_namespace(clusterns)
api.add_namespace(nodens)
api.add_namespace(namespacens)
api.add_namespace(metricsns)
api.add_namespace(clustermetricsns)
