import json

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        x = 0
        y = 1
        for _ in range(2, n + 1):
            x, y = y, x + y
        return int(y)  # Return the result as an integer.

def lambda_handler(event, context):
    try:
        # Get 'n' from input
        n = int(event['queryStringParameters']['n'])
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Missing "n" parameter.'})
        }
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Please enter a valid integer for "n".'})
        }

    # Call Function
    result = fibonacci(n)

    # Return result as JSON as it is used for lambda function
    return {
        'statusCode': 200,
        'body': json.dumps({'result': result})
    }