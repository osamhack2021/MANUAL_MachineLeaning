# AzureML 매뉴얼

## Github CodeSpace내 개발환경 유지를 위해 devcontainer 를 구성 합니다.
[Devcontainer 구성 link](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project)


## 데모 파일 구성 설명

1. test_azureml.py(실행 파일)
- Azure Machine Learing 에 필요한 정보를 담고 있으며 pytorch_train.py 파일과 같은 학습과 관련된 알고리즘 파일을 컨테이너라이즈 하여 AzureML에 전달 합니다.

```
# test_azureml.py
subscription_id = 'b6b856d1-f0e1-4d39-b0b3-4c2e1cd912cd' #예시 이며 각팀에 정보 전달 드렸습니다.
resource_group  = 'OSAM2021_ML' #예시 이며 각팀에 정보 전달 드렸습니다.
workspace_name  = 'OSAM2021_ML' #예시 이며 각팀에 정보 전달 드렸습니다.
cluster_name = "mlnode" #예시 이며 각팀에 정보 전달 드렸습니다.

# Specify a GPU base image
DEPLOY_CONTAINER_FOLDER_PATH = 'Tutorial-pytorch-birds'
SCRIPT_FILE_TO_EXECUTE = 'pytorch_train.py' # 학습할 파일
PATH_TO_YAML_FILE='./conda_dependencies.yml' # conda 세팅 yml

pytorch_env = Environment.from_conda_specification(name='pytorch_env', file_path=PATH_TO_YAML_FILE)
#pytorch_env.docker.enabled = True

pytorch_env.docker.base_image = 'mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.1-cudnn8-ubuntu18.04' # 컨테이너라이즈 되는 이미지
# Finally, use the environment in the ScriptRunConfig:
src = ScriptRunConfig(source_directory=DEPLOY_CONTAINER_FOLDER_PATH,
                      script=SCRIPT_FILE_TO_EXECUTE,
                      arguments=['--num_epochs', 30, '--output_dir', './outputs'],
                      compute_target=compute_target,
                      environment=pytorch_env)
```

2. pytorch_train.py 
- pytorch에서 제공하는 예제 파일 입니다.
https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html


## AzureML 메뉴얼
1. Pytorch (데모 구성에 사용된 예제 입니다.)
https://docs.microsoft.com/ko-kr/azure/machine-learning/how-to-train-pytorch

2. Keras
https://docs.microsoft.com/ko-kr/azure/machine-learning/how-to-train-tensorflow

3. TensorFlow
https://docs.microsoft.com/ko-kr/azure/machine-learning/how-to-train-keras

## Github CodeSpace 구성
```
# 1. DevContainer를 구성 합니다.
# 2. conda를 아래 명령어를 통해 세팅 합니다. 
$sudo conda install -c r -y conda python=3.6.2 pip=20.1.1
# 3. pip install 을 통해 의존 파일을 설치 합니다. 각 예제를 따릅니다.
```

