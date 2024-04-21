# Fibonacci REST API

## Overview
This is a basic REST API hosted in python (flask application) that computes and returns the nth number in the Fibonacci sequence. 
I have included examples of a docker deployment and lambda code which I will reference later. 

The REST API can be reached via the paths "/" or "/fibonacci".

## Considerations
This being a REST API I wanted to keep the function code as simple as possible. 
I did not use recursion for the fibonacci function as it could lead to performance issues and use unecessary resource useage (memory) once deployed. 

Especially when considering deployments like Kubernetes or AWS Fargate which may have memory or CPU thresholds for scalability.

I used flask as it is a simple way of hosting an application but it is not suitable for production deployment and would need more refinement.

## How to Run in Flask
To run the Fibonacci REST API locally using Flask, follow these steps:

1. Make sure you have Python installed on your machine.

2. Install the required dependencies:

    ```pip install -r requirements.txt```

3. Run the Flask application:

    ```python app.py```
    
4. Once the Flask application is running, you can access the API endpoint at:

    ```http://localhost:5000/?n=<integer>```

**Note:** Please remove `host='0.0.0.0'` from the `app.py` file (line 26) if you do not wish to run the application on all hosts.
    
## How to Deploy
To deploy the Fibonacci REST API using Docker, follow these steps:

1. Build and run the Docker container using Docker Compose:

    ```docker-compose up --build```

2. Once the container is up and running, you can access the API endpoint at:

    ```http://localhost:3000/?n=<integer>```

## Endpoints

### Fibonacci Endpoint
- **Endpoint:** `/` or `/fibonacci`
- **Description:** Calculates the Fibonacci value for the specified number.
- **HTTP Method:** GET
- **Status Code:** 200 OK
- **Parameters:**
  - `number` (query parameter): Integer for which Fibonacci value is calculated.
- **Response:** String format: `<number>`

**Note:** I wanted to return as a JSON format, but it was not in the specification. For the lambda, I thought JSON was appropriate.


