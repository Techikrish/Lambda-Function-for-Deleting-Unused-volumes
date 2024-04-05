import boto3

def lambda_handler(event, context):
  # Configure boto3 clients
  ec2_client = boto3.client('ec2')

  # Get all volumes
  volumes = ec2_client.describe_volumes()['Volumes']

  # Iterate through volumes
  for volume in volumes:
    # Check if volume is in a state indicating it's not in use
    if volume['State'] not in ['in-use', 'attached']:
      volume_id = volume['VolumeId']
      
      # Optional: Check for tags or other criteria before deletion
      # if has_required_tags(volume):  # Implement your tag-checking logic
      #   continue  # Skip deletion if it has specific tags
      
      # Delete unused volume
      print(f"Deleting unused volume: {volume_id}")
      ec2_client.delete_volume(VolumeId=volume_id)

  return {'message': 'Unused volume cleanup completed'}
