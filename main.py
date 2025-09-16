## These lines allow you to use FastAPI, which helps in creating 
# web applications. HTTPException is for sending errors back to the UI.
# BaseModel defines what our data should look like.
# random is for generating random numbers (for shuffling).
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import random 
#class Flashcard(BaseModel):
    #id: int
    #question: str
    #answer: str

app = FastAPI()

flashcards = [
  {
    "id": 1,
    "question": "What is the AWS service that provides a scalable relational database service?",
    "answer": "Amazon RDS"
  },
  {
    "id": 2,
    "question": "What is the primary benefit of the AWS Cloud?",
    "answer": "Trading capital expense for variable expense"
  },
  {
    "id": 3,
    "question": "Which AWS service is used to launch virtual servers in the cloud?",
    "answer": "Amazon EC2"
  },
  {
    "id": 4,
    "question": "Which of the following is a managed NoSQL database service?",
    "answer": "Amazon DynamoDB"
  },
  {
    "id": 5,
    "question": "What is the fundamental difference between a Region and an Availability Zone?",
    "answer": "A Region is a geographic area with multiple Availability Zones, while an Availability Zone is a single data center."
  },
  {
    "id": 6,
    "question": "What is a key security principle of the Shared Responsibility Model?",
    "answer": "AWS is responsible for security OF the cloud, and the customer is responsible for security IN the cloud."
  },
  {
    "id": 7,
    "question": "Which AWS service helps you monitor your AWS resources and applications?",
    "answer": "Amazon CloudWatch"
  },
  {
    "id": 8,
    "question": "Which service is a content delivery network (CDN) that delivers data with low latency?",
    "answer": "Amazon CloudFront"
  },
  {
    "id": 9,
    "question": "Which pricing model provides the most significant discount for long-term, predictable workloads?",
    "answer": "Reserved Instances"
  },
  {
    "id": 10,
    "question": "What is a security group?",
    "answer": "A virtual firewall for an EC2 instance to control inbound and outbound traffic."
  },
  {
    "id": 11,
    "question": "Which AWS service is used for long-term data archiving at the lowest cost?",
    "answer": "Amazon S3 Glacier"
  },
  {
    "id": 12,
    "question": "What is the name of the managed, serverless compute service?",
    "answer": "AWS Lambda"
  },
  {
    "id": 13,
    "question": "What is the AWS service used for user authentication and access control?",
    "answer": "AWS IAM"
  },
  {
    "id": 14,
    "question": "Which service is used to automatically adjust the number of EC2 instances in response to changing demand?",
    "answer": "Auto Scaling"
  },
  {
    "id": 15,
    "question": "What is a managed, highly scalable object storage service?",
    "answer": "Amazon S3"
  },
  {
    "id": 16,
    "question": "Which AWS service allows you to launch and manage a private network in the cloud?",
    "answer": "Amazon VPC"
  },
  {
    "id": 17,
    "question": "What is the purpose of an AWS Transit Gateway?",
    "answer": "To connect thousands of VPCs and on-premises networks to a single gateway."
  },
  {
    "id": 18,
    "question": "Which service provides a hosted DNS web service?",
    "answer": "Amazon Route 53"
  },
  {
    "id": 19,
    "question": "What is a fully managed service for building and deploying applications without managing the underlying infrastructure?",
    "answer": "AWS Elastic Beanstalk"
  },
  {
    "id": 20,
    "question": "Which AWS service helps you understand and manage your AWS spending and usage?",
    "answer": "AWS Cost Explorer"
  },
  {
    "id": 21,
    "question": "What is the AWS service for auditing and monitoring API calls in your account?",
    "answer": "AWS CloudTrail"
  },
  {
    "id": 22,
    "question": "Which AWS support plan provides access to a Technical Account Manager (TAM)?",
    "answer": "Enterprise Support"
  },
  {
    "id": 23,
    "question": "What is a service that helps protect against DDoS attacks?",
    "answer": "AWS Shield"
  },
  {
    "id": 24,
    "question": "Which AWS service provides a web application firewall (WAF)?",
    "answer": "AWS WAF"
  },
  {
    "id": 25,
    "question": "What is the service that provides recommendations for cost optimization and security?",
    "answer": "AWS Trusted Advisor"
  },
  {
    "id": 26,
    "question": "Which service is a managed data warehouse service for large-scale data analysis?",
    "answer": "Amazon Redshift"
  },
  {
    "id": 27,
    "question": "What is the AWS service that manages and stores database credentials, API keys, and other secrets?",
    "answer": "AWS Secrets Manager"
  },
  {
    "id": 28,
    "question": "Which service enables you to create and manage cryptographic keys?",
    "answer": "AWS KMS"
  },
  {
    "id": 29,
    "question": "What is the primary purpose of an Amazon Machine Image (AMI)?",
    "answer": "To provide the information required to launch an EC2 instance."
  },
  {
    "id": 30,
    "question": "Which EC2 pricing model is for temporary, flexible workloads at a significant discount?",
    "answer": "Spot Instances"
  },
  {
    "id": 31,
    "question": "Which AWS service is used to send and receive messages between software components?",
    "answer": "Amazon SQS"
  },
  {
    "id": 32,
    "question": "What is the AWS service that provides a serverless platform for data integration?",
    "answer": "AWS Glue"
  },
  {
    "id": 33,
    "question": "What is the AWS service for delivering and managing SSL/TLS certificates?",
    "answer": "AWS Certificate Manager (ACM)"
  },
  {
    "id": 34,
    "question": "Which service is a simple, scalable file storage for use with EC2 instances?",
    "answer": "Amazon EFS"
  },
  {
    "id": 35,
    "question": "What is the purpose of a TCO calculator?",
    "answer": "To compare the cost of running an on-premises infrastructure vs. AWS."
  },
  {
    "id": 36,
    "question": "Which service provides a dedicated network connection from your on-premises data center to AWS?",
    "answer": "AWS Direct Connect"
  },
  {
    "id": 37,
    "question": "What is a service for migrating databases to AWS with minimal downtime?",
    "answer": "AWS Database Migration Service (DMS)"
  },
  {
    "id": 38,
    "question": "Which AWS service provides governance, compliance, and auditing for your AWS resources?",
    "answer": "AWS Config"
  },
  {
    "id": 39,
    "question": "What is the AWS service used for container orchestration?",
    "answer": "Amazon ECS or Amazon EKS"
  },
  {
    "id": 40,
    "question": "Which AWS service provides a hybrid cloud storage service with local caching?",
    "answer": "AWS Storage Gateway"
  },
  {
    "id": 41,
    "question": "What is the AWS service for publishing and subscribing to messages?",
    "answer": "Amazon SNS"
  },
  {
    "id": 42,
    "question": "What is the benefit of using AWS Fargate?",
    "answer": "It allows you to run containers without managing servers or clusters."
  },
  {
    "id": 43,
    "question": "Which service provides a simplified, scalable platform for deploying applications?",
    "answer": "AWS Elastic Beanstalk"
  },
  {
    "id": 44,
    "question": "What is a virtual router that connects your VPC to the internet?",
    "answer": "Internet Gateway"
  },
  {
    "id": 45,
    "question": "Which service is a managed file storage service for Windows and Linux instances?",
    "answer": "Amazon FSx"
  },
  {
    "id": 46,
    "question": "Which tool provides a consolidated view of all your AWS accounts?",
    "answer": "AWS Organizations"
  },
  {
    "id": 47,
    "question": "Which service is an object storage service with multiple storage classes?",
    "answer": "Amazon S3"
  },
  {
    "id": 48,
    "question": "What is a private, scalable compute capacity in the cloud?",
    "answer": "Amazon EC2"
  },
  {
    "id": 49,
    "question": "Which AWS service is used to create and manage groups of resources that share a common tag?",
    "answer": "AWS Resource Groups"
  },
  {
    "id": 50,
    "question": "Which service allows you to run code in a serverless environment?",
    "answer": "AWS Lambda"
  },
  {
    "id": 51,
    "question": "What is the AWS service that manages the creation of resources based on a template?",
    "answer": "AWS CloudFormation"
  },
  {
    "id": 52,
    "question": "Which service is a highly available and scalable DNS web service?",
    "answer": "Amazon Route 53"
  },
  {
    "id": 53,
    "question": "What is the purpose of an Internet Gateway?",
    "answer": "To allow communication between instances in your VPC and the internet."
  },
  {
    "id": 54,
    "question": "Which EC2 pricing model is best for a steady-state, predictable workload?",
    "answer": "Reserved Instances"
  },
  {
    "id": 55,
    "question": "What is the AWS service for managing your spending and usage?",
    "answer": "AWS Cost Explorer"
  },
  {
    "id": 56,
    "question": "Which AWS service provides a managed service for data warehousing?",
    "answer": "Amazon Redshift"
  },
  {
    "id": 57,
    "question": "What is a managed, highly available relational database service?",
    "answer": "Amazon RDS"
  },
  {
    "id": 58,
    "question": "What is a managed, NoSQL database service that provides high performance at any scale?",
    "answer": "Amazon DynamoDB"
  },
  {
    "id": 59,
    "question": "Which service provides a hosted DNS web service?",
    "answer": "Amazon Route 53"
  },
  {
    "id": 60,
    "question": "Which AWS service provides recommendations for security and cost optimization?",
    "answer": "AWS Trusted Advisor"
  },
  {
    "id": 61,
    "question": "What is the AWS service that helps you monitor your AWS resources and applications?",
    "answer": "Amazon CloudWatch"
  },
  {
    "id": 62,
    "question": "Which AWS service is used for long-term data archiving at the lowest cost?",
    "answer": "Amazon S3 Glacier"
  },
  {
    "id": 63,
    "question": "What is the AWS service for auditing and monitoring API calls in your account?",
    "answer": "AWS CloudTrail"
  },
  {
    "id": 64,
    "question": "Which service is a content delivery network (CDN) that delivers data with low latency?",
    "answer": "Amazon CloudFront"
  },
  {
    "id": 65,
    "question": "What is the AWS service used for user authentication and access control?",
    "answer": "AWS IAM"
  },
  {
    "id": 66,
    "question": "Which AWS service is used to automatically adjust the number of EC2 instances in response to changing demand?",
    "answer": "Auto Scaling"
  },
  {
    "id": 67,
    "question": "What is a managed, highly scalable object storage service?",
    "answer": "Amazon S3"
  },
  {
    "id": 68,
    "question": "Which AWS service allows you to launch and manage a private network in the cloud?"
  }
]

@app.get("/flashcards")  # Tells FastAPI to run a GET request for the code below
def get_all_flashcards():  # Returns all flashcards
    return flashcards

# A new endpoint for reshuffling cards
@app.get("/flashcards/shuffle")
def shuffle_flashcards():
    random.shuffle(flashcards)
    return {"Message": "Flashcards shuffled successfully! 🎉🎉"}

# This block of code allows us to access a specific GET request by ID.
# You are able to choose a specific ID from the list.
@app.get("/flashcards/{flashcard_id}")
def get_flashcard(flashcard_id: int):
    for card in flashcards:
        if card["id"] == flashcard_id:
            return card
    raise HTTPException(status_code=404, detail="Flashcard not found 😬")
