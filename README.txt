# Memory Map: Supply Chain Dynamics and Hearing Process

* Docker reference: [GitHub: ai_job_datasets](https://github.com/denqiu/ai_job_datasets)

Setup google doc api in docker. For local file system, use the ui.

To authenticate locally, run this before starting docker (no need to run every time): run `gcloud auth application-default login --project=[PROJECT_ID] --impersonate-service-account=[SERVICE_ACCOUNT_EMAIL]`

To test: run `docker compose exec backend pytest --capture=no tests`

## Google Cloud Setup

Python:
* [quickstart](https://developers.google.com/workspace/docs/api/quickstart/python)

1. Create a project: https://developers.google.com/workspace/guides/create-project
1. No need to link billing account.
1. Enable Docs APIs.
1. Setup quota alert policies and email notification for docs read/write. Notify on 80%.
1. Create service account. No need to setup test user.
1. In IAM interface, assign yourself the Owner and Service Account Token Creator roles. Then assign service account email the Viewer role.
1. Service Accounts interface will inherit IAM principal roles so no need to edit.
1. Create WIF (Workload Identity Federation). Not Workforce, Workload. See [best practices](https://cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys?hl=en&_gl=1*1t6kjca*_ga*NDQ2MDI1NzMxLjE3NTY0MzUyODA.*_ga_WH2QY8WWF5*czE3NTgzNTEyMjUkbzE5JGcxJHQxNzU4MzUxMjU1JGozMCRsMCRoMA..) and [decision tree](https://cloud.google.com/docs/authentication?hl=en#auth-decision-tree).
    - Shell Commands
        1. `PROJECT_ID=<project-id>`
        1. `gcloud iam workload-identity-pools create "<pool-id>"   --project="${PROJECT_ID}"   --location="global"   --display-name="<Display Name>"`
        1. repository condition is required otherwise command errors out: `gcloud iam workload-identity-pools providers create-oidc "<provider-id>"   --project="${PROJECT_ID}"   --location="global"   --workload-identity-pool="<pool-id>"   --display-name="<Display Provider>"   --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.aud=assertion.aud,attribute.repository=assertion.repository" --attribute-condition="attribute.repository=='<owner>/<repo>'"  --issuer-uri="https://token.actions.githubusercontent.com"`
    - Create Workload Identity pool. https://cloud.google.com/iam/docs/workload-identity-federation?hl=en&_gl=1
    - [Blog Guide](https://cloud.google.com/blog/products/identity-security/enabling-keyless-authentication-from-github-actions)
    - [WIF Provider Conditions Setup](https://medium.com/@bbeesley/notes-on-workload-identity-federation-from-github-actions-to-google-cloud-platform-7a818da2c33e)
    - Authenticate WIF: Blog Guide and https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#authenticate
    - [Step 3 of Solution](https://github.com/orgs/community/discussions/139154#discussioncomment-10700673)
    - [GitHub Actions Auth and Detailed Setup Guide](https://github.com/google-github-actions/auth): Click arrows to expand detailed instructions on WIF via direct setup, service account setup, legacy json keys setup.
1. See Github OIDC: https://docs.github.com/en/actions/reference/security/oidc.
1. Issuer url is `issuer` value in https://token.actions.githubusercontent.com/.well-known/openid-configuration.
