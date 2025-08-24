# AWS CLI Setup Guide

To use AWS services from your local environment or scripts, you need to configure the AWS Command Line Interface (CLI) with your credentials and default region.

## Prerequisites
- Install the AWS CLI: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

## Steps to Configure AWS CLI

1. Open your terminal.
2. Run the following command:

   ```bash
   aws configure
   ```

3. You will be prompted to enter:
   - **AWS Access Key ID**: Your AWS access key.
   - **AWS Secret Access Key**: Your AWS secret key.
   - **Default region name**: e.g., `us-east-1`.
   - **Default output format**: e.g., `json` (press Enter to use default).

4. Your credentials will be saved in `~/.aws/credentials` and configuration in `~/.aws/config`.

## Example
```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: json
```

## Security Note
- Never share your AWS credentials.
- Do not commit credentials to version control.

For more details, see the [AWS CLI User Guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html).
