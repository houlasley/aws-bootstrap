# Justfile — clean, minimal, and sources .env automatically

# Source environment variables from .env
set dotenv-load

setup:
  python3 -m venv .venv && \
  source .venv/bin/activate && \
  pip install -r requirements.txt && \
  pip install aws-cdk.aws-iam "constructs>=10.0.0,<11.0.0"

clean:
  rm -rf .venv cdk.out __pycache__ *.pyc

synth:
  source .venv/bin/activate && cdk synth

deploy-dev:
  AWS_PROFILE=$DEV_PROFILE \
  CDK_DEFAULT_ACCOUNT=$DEV_ACCOUNT \
  CDK_DEFAULT_REGION=$DEV_REGION \
  source .venv/bin/activate && \
  cdk deploy GitHubActionsBootstrapStack --require-approval never --profile $DEV_PROFILE

deploy-prod:
  AWS_PROFILE=$PROD_PROFILE \
  CDK_DEFAULT_ACCOUNT=$PROD_ACCOUNT \
  CDK_DEFAULT_REGION=$PROD_REGION \
  source .venv/bin/activate && \
  cdk deploy GitHubActionsBootstrapStack --require-approval never --profile $PROD_PROFILE

bootstrap-dev:
  AWS_PROFILE=$DEV_PROFILE \
  cdk bootstrap aws://$DEV_ACCOUNT/$DEV_REGION --profile $DEV_PROFILE

bootstrap-prod:
  AWS_PROFILE=$PROD_PROFILE \
  cdk bootstrap aws://$PROD_ACCOUNT/$PROD_REGION --profile $PROD_PROFILE
