""" Init """
import os
import yaml
import logging

# Check if development or containerized environment
# Load environment variables from file, if local i.e. 'iscontainer' env variable is not set
is_runtime_container_key = 'runtime_iscontainer'
if not os.getenv(is_runtime_container_key) or os.getenv(is_runtime_container_key) != 'True':
    cnfg = yaml.load(
        open('config.local.yaml'),
        Loader=yaml.SafeLoader)['envvars']
    os.environ.update(cnfg)
    logging.info("environment update from config.local.yaml")
else:
    logging.info("runtime_iscontainer environment variable is set")
