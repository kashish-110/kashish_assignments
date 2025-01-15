import json

def lambda_handler(event, context):
    # Extracting numbers from the event object
    a = int(event.get('a', 5))  # Default to 0 if 'a' is not provided
    b = int(event.get('b', 6))  # Default to 0 if 'b' is not provided

    # Performing addition
    c = a + b

    # Returning the result
    return {
        'statusCode': 200,
        'body': json.dumps(f'The result is {c}')
    }
