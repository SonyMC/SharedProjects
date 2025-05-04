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

	- login : sonymathew_dev


(2) Set Up the AWS CLI and AWS SDKs
	- https://docs.aws.amazon.com/textract/latest/dg/setup-awscli-sdk.html
		- Java: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/home.html


(3) Setup Overview:
	- https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
	

(4) Configure AWS CLI:
	Note: Have used IAM user sonymathew_dev
	
	Open powershell(admin):
	- cmd: aws configure

AWS Access Key ID [****************MUVL]: xxxx
AWS Secret Access Key [****************uAwX]: xxxx
Default region name [us-east-1]:
Default output format [json]:





(5) Create the project:

 cmd: mvn archetype:generate "-DarchetypeGroupId=software.amazon.awssdk" "-DarchetypeArtifactId=archetype-app-quickstart" -"DarchetypeVersion=2.16.3"

(5)Enter the value listed in the second column for each prompt.

Prompt	Value to enter
Define value for property 'service':	s3
Define value for property 'httpClient':	apache-client
Define value for property 'nativeImage':	false
Define value for property 'groupId':	com.mailsonymathew
Define value for property 'artifactId':	getstarted
Define value for property 'version' 1.0-SNAPSHOT:	<Enter>
Define value for property 'package' org.example:	<Enter>


(6)After the last value is entered, Maven lists the choices you made. Confirm by entering Y or re-enter values by entering N.

Maven creates the project folder named getstarted based on the artifactId value that you entered. Inside the getstarted folder, find a README.md file that you can review, a pom.xml file, and a src directory.


(7)Make teh code changes as described in "Step 3 - Write the code" section of  https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html


(8) Build and run the application
mvn clean package

(9) Open IDE ( IntellIJ) and run App.java


(10) 
To view the new bucket and object that the program creates, perform the following steps.

In Handler.java, comment out the line cleanUp(s3Client, bucket, key) in the sendRequest method and save the file.

Rebuild the project by running mvn clean package.

Rerun App.java

Sign in to the S3 console to view the new object in the newly created bucket.

