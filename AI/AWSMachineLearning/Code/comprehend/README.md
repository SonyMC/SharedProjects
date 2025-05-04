# Intro:
Amazon Comprehend is a natural language processing (NLP) service that uses machine learning (ML) to find insights and relationships in texts. Amazon Comprehend identifies the language of the text; extracts key phrases, places, people, brands, or events; and understands how positive or negative the text is. For more information about everything Amazon Comprehend can do, see Amazon Comprehend Features.


##Preparing data:
https://aws.amazon.com/blogs/machine-learning/building-a-custom-classifier-using-amazon-comprehend/



## S3 bucket used: 
sm-dev-ai 


##Download training files:
\Code\comprehend

cmd: aws s3 cp s3://aws-ml-blog/artifacts/comprehend-custom-classification/comprehend-test.csv . 
cmd: aws s3 cp s3://aws-ml-blog/artifacts/comprehend-custom-classification/comprehend-train.csv 



The files train.csv and test.csv contain the training samples as comma-separated values. There are four columns in them, corresponding to class index (1 to 10), question title, question content, and best answer. The text fields are escaped using double quotes (“), and any internal double quote is escaped by two double quotes (“”). New lines are escaped by a backslash followed with an “n” character, that is “\n”.


##Upload Training FIles to S3 bucket:

cmd: aws s3 cp comprehend-train.csv s3://sm-dev-ai/
cmd: aws s3 cp comprehend-test.csv s3://sm-dev-ai/






## Training the custom classifier ( Create Document Classifier)
cmd:
aws comprehend create-document-classifier --document-classifier-name "sony-answer3" --data-access-role-arn arn:aws:iam::nnn:role/sm-dev-comprehend-role --input-data-config S3Uri=s3://sm-dev-ai/comprehend-train.csv --output-data-config S3Uri=s3://sm-dev-ai/TrainingOutput/ --language-code en

Response:
{
    "DocumentClassifierArn": "arn:aws:comprehend:us-east-1:nnn:document-classifier/sony-answer3"
}


## It is an asynchronous call. You can then track the training progress with the following command:
cmd:
aws comprehend describe-document-classifier --document-classifier-arn arn:aws:comprehend:us-east-1:nnn:document-classifier/sony-answer3

    "DocumentClassifierProperties": {
        "DocumentClassifierArn": "arn:aws:comprehend:us-east-1:nnn:document-classifier/sony-answer3",
        "LanguageCode": "en",
        "Status": "SUBMITTED",
        "SubmitTime": "2024-07-05T12:38:51.886000+05:30",
        "InputDataConfig": {
            "DataFormat": "COMPREHEND_CSV",
            "S3Uri": "s3://sm-dev-ai/comprehend-train.csv"
        },
        "OutputDataConfig": {
            "S3Uri": "s3://sm-dev-ai/TrainingOutput/nnn-CLR-af4cd375e88ae5a69875ce800450ddf0/output/output.tar.gz"
        },
        "DataAccessRoleArn": "arn:aws:iam::nnn:role/sm-dev-comprehend-role",
        "Mode": "MULTI_CLASS"
    }
}



## Amazon Comprehend Dashboard:
AWS -> Amazon Comprehend -> Custom Classifictaion -> Classifier modes -> sony-answer3

The training duration may vary; in this case, the training took approximately one hour for the full dataset (20 minutes for the reduced dataset).

The output for the training on the full dataset shows that your model has a recall of 0.72—in other words, it correctly identifies 72% of given labels.


** Note: Remember to stop the classifier if you do not want to incur charges.

# Amazon Comprehend code examples for the SDK for Java 2.x

## Overview

Shows how to use the AWS SDK for Java 2.x to work with Amazon Comprehend.

<!--custom.overview.start-->
<!--custom.overview.end-->

_Amazon Comprehend uses natural language processing (NLP) to extract insights about the content of documents without the need of any special preprocessing._

## ⚠ Important

* Running this code might result in charges to your AWS account. For more details, see [AWS Pricing](https://aws.amazon.com/pricing/) and [Free Tier](https://aws.amazon.com/free/).
* Running the tests might result in charges to your AWS account.
* We recommend that you grant your code least privilege. At most, grant only the minimum permissions required to perform the task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege).
* This code is not tested in every AWS Region. For more information, see [AWS Regional Services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services).

<!--custom.important.start-->
<!--custom.important.end-->

## Code examples

### Prerequisites

For prerequisites, see the [README](../../README.md#Prerequisites) in the `javav2` folder.


<!--custom.prerequisites.start-->
<!--custom.prerequisites.end-->

### Single actions

Code excerpts that show you how to call individual service functions.

- [CreateDocumentClassifier](src/main/java/com/example/comprehend/DocumentClassifierDemo.java#L6)
- [DetectDominantLanguage](src/main/java/com/example/comprehend/DetectLanguage.java#L6)
- [DetectEntities](src/main/java/com/example/comprehend/DetectEntities.java#L6)
- [DetectKeyPhrases](src/main/java/com/example/comprehend/DetectKeyPhrases.java#L6)
- [DetectSentiment](src/main/java/com/example/comprehend/DetectSentiment.java#L6)
- [DetectSyntax](src/main/java/com/example/comprehend/DetectSyntax.java#L6)


<!--custom.examples.start-->
<!--custom.examples.end-->

## Run the examples

### Instructions


<!--custom.instructions.start-->
<!--custom.instructions.end-->



### Tests

⚠ Running tests might result in charges to your AWS account.


To find instructions for running these tests, see the [README](../../README.md#Tests)
in the `javav2` folder.



<!--custom.tests.start-->
<!--custom.tests.end-->

## Additional resources

- [Amazon Comprehend Developer Guide](https://docs.aws.amazon.com/comprehend/latest/dg/what-is.html)
- [Amazon Comprehend API Reference](https://docs.aws.amazon.com/comprehend/latest/APIReference/welcome.html)
- [SDK for Java 2.x Amazon Comprehend reference](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/comprehend/package-summary.html)

<!--custom.resources.start-->
<!--custom.resources.end-->

---

Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.

SPDX-License-Identifier: Apache-2.0