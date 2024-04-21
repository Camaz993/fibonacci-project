# Fibonacci REST API

## Overview
This is a basic REST API hosted in python (flask application) that computes and returns the nth number in the Fibonacci sequence. 
I have included examples of a docker deployment and lambda code which I will reference later. 

The REST API can be reached via the paths "/" or "/fibonacci".

## Considerations
This being a REST API I wanted to keep the function code as simple as possible. 
I did not use recursion for the fibonacci function as it could lead to performance issues and use unecessary resource useage (memory) once deployed. 

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

## Production Deployment Considerations

In this section I will describe how I would deploy such an application in a production environment. I would deploy into AWS Cloud infastructure but I will also mention Azure as well.

### Containerization / Lambda

Firstly, for such a task where there is only one primary function I believe creating a docker container isn't necessary. Although it is a great way of hosting the REST API a serverless approach, e.g. single lambda function or Azure function, might be more appropriate given the simplicity. You could argue the same point for a API Gateway or API management plane that points to only one function as well, but by just having a lambda function it would reduce the complexity of deployment and dependancies on docker (runtime, container repository etc). 

Because the document asked for details on containerization I have included a basic docker-compose.yml file which could be used to host the application. Since the application does have many depandancies a base python image can be used and depending on was application service is used (e.g. flask) it can be installed via the requirements.txt file. For a small application like this I would want to keep the amount of dependancies to a minimum so that there is less management involved (e.g. updates or package vulnerabilities).

The docker image could then be hosted in a cloud repository such as ECS or Azure Container Apps.

### CICD 

I will describe two different approaches for deployment; A serverless version and a docker version.

## Serverless

Bitbucket Pipelines would be appropriate for deploying the serverless application. This would use isolated Docker images or workers for deployments. CI/CD principles would be upheld, with feature or bugfix branches being deployed to a development environment once a pull request is approved. I would consider deployments to development to be manual depending on the size of the development team, as you do not want dev environments to constantly be deploying. The next branch would be Master. When a pull request is approved and merged into the Master or Main branch, development and UAT environments would automatically deploy in parallel. After this, production environments would be deployed manually and specified in a step to run in parallel.

Cloud resources would be specified in CloudFormation templates, which would be separated into a different folder in the directory. These would be deployed before the serverless functions in the Bitbucket Pipelines and could be executed via script statements (e.g., AWS CLI). The serverless file (serverless.yml) would hold contents for deploying the different Lambda functions and would reference any cloud resources. Separating the resources allows for the use of environment variables to uphold naming conventions and reduce deployment code.

## Docker

I would follow the same branch-based deployment scheme above. Bitbucket Pipelines or Azure DevOps would be a suitable choice for deploying the CICD pipelines. Both would involve building and pushing the Docker image to a container repository. From there, other resources could be deployed to host the Docker-based application, such as AWS Fargate or AKS Ingress.

### Logging and Monitoring

Logging: Implement logging throughout your codebase using Python's "logging" module or Flask's built-in logging capabilities. Configure log levels, formats, and destinations to capture relevant information about application events, errors, and performance metrics. Since the applications features are limitted I would only log input (n) and error output. Since you know the input and if the function is successful there is no need to log the fibonacci numbers themselves. This is because it could expose you to large log storage files. Store logs centrally in services like AWS CloudWatch or Azure Monitor for analysis. 

Monitoring: Utilize services like AWS CloudWatch or Azure Monitor to monitor the health, performance, and availability of your application. Set up alarms and notifications for critical metrics such as response times, error rates, and resource utilization to proactively detect and address issues.

### Scalability

I will consider both function (lambda) and container-based deployments. Another benefit of deploying the service as a function is that horizontal scalability is very easy. For AWS Lambda functions, the service will scale automatically based on the number of requests. If no provision concurrency is configured, then the application will run from a cold start. However, since it is extremely lightweight with no recursion and dependencies (no need for Flask), it should be very fast. To advance scalability, you could always add provision concurrency for "hot" Lambda functions.

For container-based deployments, I would use either AWS Fargate or Azure Container Instances. This is mainly so that you don't have to manage underlying infrastructure, and they provide a serverless experience. AKS or EKS might be considered overkill. However, if you anticipate significant growth or plan to integrate the Fibonacci application into a larger containerized environment, Kubernetes could be a suitable option for future-proofing and scalability.

