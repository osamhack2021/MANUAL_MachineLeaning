# AzureML 매뉴얼

## Github CodeSpace내 개발환경 유지를 위해 devcontainer 를 구성 합니다.
[Devcontainer 구성 link](https://docs.github.com/en/codespaces/customizing-your-codespace/configuring-codespaces-for-your-project)


## 데모 파일 구성 설명

1. test_azureml.py(실행 파일)
- Azure Machine Learing 에 필요한 정보를 담고 있으며 pytorch_train.py 파일과 같은 학습과 관련된 알고리즘 파일을 컨테이너라이즈 하여 AzureML에 전달 합니다.

```python
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

## Azure Machine Learning 사용법

### 1. 팀 별 유저 초대
- 아래 이미지와 같이 각 팀 인원 메일을 통해 초대 하였습니다.
![img_](https://user-images.githubusercontent.com/22819926/135014741-3c03aca6-dbd0-4988-9721-a0b2b290a1cf.png)

### 2. Github CodeSpace 에서 실행
- MS에서 제공된 컨테이너 기반으로 Docker 빌드가 발생하며 학습해야하는 파일을 포함하여 Azure Machine Learing Service 에 제출 합니다.
- Container 커스텀 빌드시 CUDA 버전 확인 바랍니다. 타켓 디바이스는 Nvidia V100 입니다.
![img_](https://user-images.githubusercontent.com/22819926/135014743-e79f1033-6be0-4b4d-8bc1-cc540e4a234e.png)

### 3. 실험 결과 확인 및 모델 파일 다운 로드
- 각 팀마다 제공드린 Azure Machine Learing Service 유니크 URL 을 통해 실험내역과 모델 파일을 다운 받을 수 있습니다. (Jupyter 서버는 별도 제공하지 않습니다.)
- 제공되는 클러스터 성능은  vCPU 6, 112GB RAM, 336GB Disk, Nvidia V100 입니다.
![img_](https://user-images.githubusercontent.com/22819926/135014746-a91426fa-112d-43d3-81af-cb214cd8c68c.png)
![img_](https://user-images.githubusercontent.com/22819926/135014744-d6c952e0-caa9-47ba-a211-227c66c2d406.png)
![img_](https://user-images.githubusercontent.com/22819926/135014739-fec505a6-7fd2-4938-95b8-675fc6427143.png)

