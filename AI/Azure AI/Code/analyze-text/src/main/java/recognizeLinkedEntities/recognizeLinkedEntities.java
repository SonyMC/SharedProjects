package recognizeLinkedEntities;

import com.azure.ai.textanalytics.TextAnalyticsClient;
import com.azure.ai.textanalytics.TextAnalyticsClientBuilder;
import com.azure.core.credential.AzureKeyCredential;

/*
Refer https://learn.microsoft.com/en-us/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-stable#analyze-sentiment
*/
 /*
Note : Create language instance before running this and update the key and endpoint
*/
/*
Linked entities identifies and clarifies then meaning of specific entities(like people, places, or organizations) found in text by linking them to the Wikipedia data source.
*/

public class recognizeLinkedEntities {

    private static final String key = "xxxx";
    private static final String endpoint = "https://xxxx-lang-instance.cognitiveservices.azure.com";

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

        String document1 = "Old Faithful is a geyser at Yellowstone Park.";
        System.out.println(document1);
        textAnalyticsClient.recognizeLinkedEntities(document1).forEach(linkedEntity -> {
            System.out.println("Linked Entities:");
            System.out.printf("Name: %s, entity ID in data source: %s, URL: %s, data source: %s.%n",
                    linkedEntity.getName(), linkedEntity.getDataSourceEntityId(), linkedEntity.getUrl(), linkedEntity.getDataSource());
            linkedEntity.getMatches().forEach(match ->
                    System.out.printf("Text: %s, confidence score: %f.%n", match.getText(), match.getConfidenceScore()));
        });


        System.out.println("************************\n" );

        String document2 = "Technopark is an IT park in Trivandrum";
        System.out.println(document2);
        textAnalyticsClient.recognizeLinkedEntities(document2).forEach(linkedEntity -> {
            System.out.println("Linked Entities:");
            System.out.printf("Name: %s, entity ID in data source: %s, URL: %s, data source: %s.%n",
                    linkedEntity.getName(), linkedEntity.getDataSourceEntityId(), linkedEntity.getUrl(), linkedEntity.getDataSource());
            linkedEntity.getMatches().forEach(match ->
                    System.out.printf("Text: %s, confidence score: %f.%n", match.getText(), match.getConfidenceScore()));
        });


    }
}


