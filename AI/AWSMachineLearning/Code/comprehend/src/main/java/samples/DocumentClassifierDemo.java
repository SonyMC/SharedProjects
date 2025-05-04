// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

package samples;

import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.comprehend.ComprehendClient;
import software.amazon.awssdk.services.comprehend.model.ComprehendException;
import software.amazon.awssdk.services.comprehend.model.CreateDocumentClassifierRequest;
import software.amazon.awssdk.services.comprehend.model.CreateDocumentClassifierResponse;
import software.amazon.awssdk.services.comprehend.model.DocumentClassifierInputDataConfig;


/**
 * Before running this code example, you can setup the necessary resources, such
 * as the CSV file and IAM Roles, by following this document:
 * https://aws.amazon.com/blogs/machine-learning/building-a-custom-classifier-using-amazon-comprehend/
 *
 * Also, set up your development environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DocumentClassifierDemo {
    public static void main(String[] args) {
        //final String usage = "textract/src/main/resources/sample.jpg";


        String dataAccessRoleArn = "arn:aws:iam::172172108913:role/sonymathew-dev-comprehend-role"; // Role: arn of role with "ComprehendDataAccessRolePolicy" policy configured
        String s3Uri = "s3://sonymathew-dev-ai/comprehend-test.csv";
        String documentClassifierName = "sony-answer3"; // documentClassifierName (Refer README.md )

        Region region = Region.US_EAST_1;
        ComprehendClient comClient = ComprehendClient.builder()
                .region(region)
                .build();

        createDocumentClassifier(comClient, dataAccessRoleArn, s3Uri, documentClassifierName);
        comClient.close();
    }

    public static void createDocumentClassifier(ComprehendClient comClient, String dataAccessRoleArn, String s3Uri,
                                                String documentClassifierName)
    {
        try {
            DocumentClassifierInputDataConfig config = DocumentClassifierInputDataConfig.builder()
                    .s3Uri(s3Uri)
                    .build();

            DocumentClassifierInputDataConfig config1 = DocumentClassifierInputDataConfig.builder().build()

            CreateDocumentClassifierRequest createDocumentClassifierRequest = CreateDocumentClassifierRequest.builder()
                    .documentClassifierName(documentClassifierName)
                    .dataAccessRoleArn(dataAccessRoleArn)
                    .languageCode("en")
                    .inputDataConfig(config)
                    .build();

            CreateDocumentClassifierResponse createDocumentClassifierResult = comClient
                    .createDocumentClassifier(createDocumentClassifierRequest);
            String documentClassifierArn = createDocumentClassifierResult.documentClassifierArn();
            System.out.println("Document Classifier ARN: " + documentClassifierArn);

        } catch (ComprehendException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
}
// snippet-end:[comprehend.java2.classifier.main]