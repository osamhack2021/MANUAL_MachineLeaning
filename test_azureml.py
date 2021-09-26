import os
import shutil

from azureml.core.workspace import Workspace
from azureml.core import Experiment
from azureml.core import Environment

from azureml.core.compute import ComputeTarget, AmlCompute
from azureml.core.compute_target import ComputeTargetException
from azureml.core.authentication import InteractiveLoginAuthentication

from azureml.core import ScriptRunConfig
from azureml.core.runconfig import DockerConfiguration

interactive_auth = InteractiveLoginAuthentication(tenant_id="a364d1c3-2922-45c9-bd72-87a573f412c6")
subscription_id = 'b6b856d1-f0e1-4d39-b0b3-4c2e1cd912cd'
resource_group  = 'OSAM2021_ML'
workspace_name  = 'OSAM2021_ML'
cluster_name = "mlnode"

try:
    ws = Workspace(subscription_id = subscription_id, resource_group = resource_group, workspace_name = workspace_name)
    ws.write_config()
    print('Library configuration succeeded')
except:
    print('Workspace not found')

project_folder = './Tutorial-pytorch-birds'
os.makedirs(project_folder, exist_ok=True)
shutil.copy('./pytorch_train.py', project_folder)


try:
    compute_target = ComputeTarget(workspace=ws, name=cluster_name)
    print('Found existing compute target')
except ComputeTargetException:
    print('Not Found Exsiting Target Cluster')

# Specify a GPU base image
DEPLOY_CONTAINER_FOLDER_PATH = 'Tutorial-pytorch-birds'
SCRIPT_FILE_TO_EXECUTE = 'pytorch_train.py'
PATH_TO_YAML_FILE='./conda_dependencies.yml'

pytorch_env = Environment.from_conda_specification(name='pytorch_env', file_path=PATH_TO_YAML_FILE)
#pytorch_env.docker.enabled = True

pytorch_env.docker.base_image = 'mcr.microsoft.com/azureml/openmpi3.1.2-cudas11.0-cudnn7-ubuntu18.04'
# Finally, use the environment in the ScriptRunConfig:
src = ScriptRunConfig(source_directory=DEPLOY_CONTAINER_FOLDER_PATH,
                      script=SCRIPT_FILE_TO_EXECUTE,
                      arguments=['--num_epochs', 30, '--output_dir', './outputs'],
                      compute_target=compute_target,
                      environment=pytorch_env)

run = Experiment(ws, name='Tutorial-pytorch-birds').submit(src)
run.wait_for_completion(show_output=True)