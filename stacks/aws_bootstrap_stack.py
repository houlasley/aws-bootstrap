from aws_cdk import (
    Stack,
)
from aws_cdk import (
    aws_iam as iam,
)
from constructs import Construct


class GitHubActionsBootstrapStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, repo_name: str, **kwargs):
        super().__init__(scope, construct_id, **kwargs)

        oidc_provider = iam.OpenIdConnectProvider(
            self,
            "GitHubOIDCProvider",
            url="https://token.actions.githubusercontent.com",
            client_ids=["sts.amazonaws.com"],
        )

        iam.Role(
            self,
            "GitHubActionsDeployRole",
            role_name="github-actions-deploy",
            assumed_by=iam.WebIdentityPrincipal(
                oidc_provider.open_id_connect_provider_arn,
                conditions={
                    "StringLike": {
                        "token.actions.githubusercontent.com:sub": f"repo:{repo_name}/*"
                    }
                },
            ),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("AdministratorAccess")
            ],
        )
