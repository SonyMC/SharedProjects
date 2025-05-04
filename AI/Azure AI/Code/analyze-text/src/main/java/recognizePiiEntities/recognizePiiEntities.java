package recognizePiiEntities;

import com.azure.ai.textanalytics.TextAnalyticsAsyncClient;
import com.azure.ai.textanalytics.TextAnalyticsClient;
import com.azure.ai.textanalytics.TextAnalyticsClientBuilder;
import com.azure.ai.textanalytics.models.PiiEntityCollection;
import com.azure.core.credential.AzureKeyCredential;
/*
Refer https://learn.microsoft.com/en-us/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-stable#analyze-sentiment
 */
public class recognizePiiEntities {

    /*
    Note : Create language instance before running this and update the key and endpoint
    */
    private static final String key = "xxxx";
    private static final String endpoint = "https://xxxx.cognitiveservices.azure.com";

    public static void main(String[] args) {

        TextAnalyticsClient textAnalyticsClient = new TextAnalyticsClientBuilder()
                .credential(new AzureKeyCredential(key))
                .endpoint(endpoint)
                .buildClient();

        // Async/Non Blocking Client
//        TextAnalyticsAsyncClient textAnalyticsAsyncClient = new TextAnalyticsClientBuilder()
//                .credential(new AzureKeyCredential(key))
//                .endpoint(endpoint)
//                .buildAsyncClient();

        System.out.println("************************\n" );

        String document1 = "My SSN is 859-98-0987";
        System.out.println(document1);
        PiiEntityCollection piiEntityCollection1 = textAnalyticsClient.recognizePiiEntities(document1);
        System.out.printf("Redacted Text: %s%n", piiEntityCollection1.getRedactedText());
        piiEntityCollection1.forEach(entity -> System.out.printf(
                "Recognized Personally Identifiable Information entity: %s, entity category: %s, entity subcategory: %s,"
                        + " confidence score: %f.%n",
                entity.getText(), entity.getCategory(), entity.getSubcategory(), entity.getConfidenceScore()));

        System.out.println("************************\n" );

        String document2 = "My phone no. is 1122334455";
        System.out.println(document2);
        PiiEntityCollection piiEntityCollection2 = textAnalyticsClient.recognizePiiEntities(document2);
        System.out.printf("Redacted Text: %s%n", piiEntityCollection2.getRedactedText());
        piiEntityCollection2.forEach(entity -> System.out.printf(
                "Recognized Personally Identifiable Information entity: %s, entity category: %s, entity subcategory: %s,"
                        + " confidence score: %f.%n",
                entity.getText(), entity.getCategory(), entity.getSubcategory(), entity.getConfidenceScore()));


        System.out.println("************************\n" );

        String document3 = "I was born on 01 April, 1985";
        System.out.println(document3);
        PiiEntityCollection piiEntityCollection3 = textAnalyticsClient.recognizePiiEntities(document3);
        System.out.printf("Redacted Text: %s%n", piiEntityCollection3.getRedactedText());
        piiEntityCollection3.forEach(entity -> System.out.printf(
                "Recognized Personally Identifiable Information entity: %s, entity category: %s, entity subcategory: %s,"
                        + " confidence score: %f.%n",
                entity.getText(), entity.getCategory(), entity.getSubcategory(), entity.getConfidenceScore()));

    }
}

