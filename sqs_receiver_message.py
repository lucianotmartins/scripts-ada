
import boto3

def consume_queue():
    sqs_client = boto3.client('sqs', region_name='us-east-1')
    response = sqs_client.receive_message(
        QueueUrl="https://sqs.us-east-1.amazonaws.com/account/letscode-app",
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10
    )
    
    print (response)

if __name__ == '__main__':

    response = consume_queue()
