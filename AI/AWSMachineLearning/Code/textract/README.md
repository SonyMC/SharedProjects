# Refer: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html

# App

This project contains a maven application with [AWS Java SDK 2.x](https://github.com/aws/aws-sdk-java-v2) dependencies.

## Prerequisites
- Java 1.8+
- Apache Maven
- GraalVM Native Image (optional)


## Objective:
- Create a S3 bucket, upload an object and deelte the buckets

Steps:


(1)Create a user with administrative access

	- https://docs.aws.amazon.com/textract/latest/dg/setting-up.html

	- login : sm_dev


(2) Set Up the AWS CLI and AWS SDKs
	- https://docs.aws.amazon.com/textract/latest/dg/setup-awscli-sdk.html
		- Java: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html


(3) Setup Overview:
	- https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
	

(4) Configure AWS CLI:
	Note: Have used IAM user sm_dev
	
	Open powershell(admin):
	- cmd: aws configure

AWS Access Key ID [****************MUVL]: xxxx
AWS Secret Access Key [****************uAwX]: xxxx
Default region name [us-east-1]:
Default output format [json]:





(5) Create new mavenmodule in IDE:


(6) Update POM.xm:
	https://github.com/awsdocs/aws-doc-sdk-examples/blob/main/javav2/example_code/textract/pom.xml


(7) Code reference:

https://docs.aws.amazon.com/textract/latest/dg/service_code_examples.html


