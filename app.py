import os

from aws_cdk import App, Environment, Tags

from stacks.aws_bootstrap_stack import GitHubActionsBootstrapStack

app = App()
# Read environment variables
account = os.environ.get("CDK_DEFAULT_ACCOUNT")
region = os.environ.get("CDK_DEFAULT_REGION")
stack = GitHubActionsBootstrapStack(
    app,
    "GitHubActionsBootstrapStack",
    repo_name="houlasley",  # replace if needed
    env=Environment(account=account, region=region),
)
# Apply tags globally to all resources in the stack
Tags.of(stack).add("Project", "aws-bootstrap")
Tags.of(stack).add("Owner", "haslou")
Tags.of(stack).add("ManagedBy", "CDK")
app.synth()
