# AWS Bootstrap CDK Project

This project sets up shared AWS infrastructure resources required to support GitHub Actions deployments using OpenID Connect (OIDC). It deploys a CDK stack that defines an IAM role with trust policies for GitHub Actions to assume and perform deployments.

## 🚀 What It Does

- Creates a GitHub OIDC IAM role for use in GitHub Actions
- Tags resources for cost tracking and ownership
- Uses CDK to manage everything as infrastructure-as-code
- Supports multiple environments (dev and prod) via a single `.env` file and `just` commands

---

## 📁 Structure

```bash
.
├── app.py                  # CDK entry point
├── bootstrap_stack.py     # Defines the GitHubActionsBootstrapStack
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables for dev and prod
├── Justfile               # Developer-friendly CLI interface
└── cdk.out/               # CDK synth output (ignored)
```

---

## ✅ Getting Started

### 1. Install dependencies

```bash
just setup
```

### 2. Configure AWS SSO profiles (if needed)

```bash
aws configure sso --profile dev-profile
aws configure sso --profile prod-profile
```

### 3. Login via SSO

```bash
just login-dev    # or just login-prod
```

### 4. Deploy to an environment

```bash
just deploy-dev    # deploys using dev-profile
just deploy-prod   # deploys using prod-profile
```

### 5. Bootstrap CDK if needed

```bash
just bootstrap-dev
just bootstrap-prod
```

---

## 🔧 Environment Config

Set your AWS account info in the `.env` file:

```ini
DEV_ACCOUNT=111122223333
DEV_PROFILE=dev-profile
DEV_REGION=us-east-1

PROD_ACCOUNT=444455556666
PROD_PROFILE=prod-profile
PROD_REGION=us-east-1
```

These values are automatically loaded by `just`.

---

## 🧪 Useful Commands

```bash
just synth              # CDK synth
just clean              # Remove build artifacts
just login-dev          # Run AWS SSO login for dev
just login-prod         # Run AWS SSO login for prod
```

---

## 🏷️ Tags
All resources include standard project ownership tags:
- `Project: aws-bootstrap`
- `Owner: haslou`
- `ManagedBy: CDK`

---

