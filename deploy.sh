#!/bin/bash
set -e

export RELEASE=$(git rev-parse --short HEAD)
export IMAGE_REPO="<docker_registry_repo>"
PROJECT_NAME="<project_name>"
ENVIRONMENT=$1
REGION="<region>"
SERVICE="<backend|frontend>"
COMPOSE_CMD="docker-compose -f deploy.yml"

command -v docker >/dev/null 2>&1 || { echo "Please install docker. See: https://docs.docker.com/install/" >&2; exit 1; }
command -v docker-compose >/dev/null 2>&1 || { echo "Please install docker-compose. See: https://docs.docker.com/compose/install/" >&2; exit 1; }
command -v aws >/dev/null 2>&1 || { echo "Please install awscli by 'pip install awscli'" >&2; exit 1; }
set +e
ssh-add -L | grep $PROJECT_NAME >/dev/null
if [ $? -ne 0 ]; then
    echo "Please add $PROJECT_NAME ssh private key to ssh-agent to proceed. E.g 'ssh-add private_key_file'"
    exit 1
fi
set -e

if [ "$ENVIRONMENT" = "prod" ]; then
  IP="<ip>"
elif [ "$ENVIRONMENT" = "stage" ]; then
  IP="<ip>"
else
  echo "Invalid environment"
  exit 1
fi
echo "IP = $IP"
echo "COMPOSE_CMD = $COMPOSE_CMD"
echo "RELEASE = $RELEASE"

aws s3 cp s3://$PROJECT_NAME-terraform-$ENVIRONMENT/$SERVICE.env .env-deploy
$COMPOSE_CMD build
$(aws ecr get-login --no-include-email --region $REGION)
$COMPOSE_CMD push

scp ./.env-deploy deploy@$IP:.env-deploy
scp ./deploy.yml deploy@$IP:$SERVICE.yml
ssh deploy@$IP "export RELEASE=$RELEASE; export IMAGE_REPO=$IMAGE_REPO; $(aws ecr get-login --no-include-email --region $REGION); docker stack deploy --with-registry-auth -c $SERVICE.yml $PROJECT_NAME-$SERVICE"
