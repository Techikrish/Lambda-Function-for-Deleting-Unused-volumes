# Lambda Function: Delete Unused EBS Volumes
### Prerequisites - 
**Lambda Function Timeout**: Set the function timeout to **10 seconds** to ensure efficient execution

**IAM Policy Permissions** Create an IAM policy with the following permissions for your Lambda function’s execution role:

    -     `ec2:DescribeVolumes`
    - -   `ec2:DeleteVolume`
    - -   'logs:PutLogEvents`: This is needed if your Lambda function writes logs to CloudWatch during execution.
   

