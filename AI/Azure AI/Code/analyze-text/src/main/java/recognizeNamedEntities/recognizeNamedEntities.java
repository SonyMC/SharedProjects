package recognizeNamedEntities;

import com.azure.ai.textanalytics.TextAnalyticsAsyncClient;
import com.azure.ai.textanalytics.TextAnalyticsClient;
import com.azure.ai.textanalytics.TextAnalyticsClientBuilder;
import com.azure.ai.textanalytics.models.DetectedLanguage;
import com.azure.core.credential.AzureKeyCredential;

/*
Refer https://learn.microsoft.com/en-us/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-stable#analyze-sentiment
 */
/*
Recognize Named Entities are the entities that are present in the text. The entities can be a person, location, organization, date, quantity, percentage, currency, or phone number.
 */
public class recognizeNamedEntities {
    /*
    Note : Create language instance before running this and update the key and endpoint
    */
    private static final String key = "xxxxx";
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

        String document1 = "Satya Nadella is the CEO of Microsoft";
        System.out.println(document1);
        textAnalyticsClient.recognizeEntities(document1).forEach(entity ->
                System.out.printf("Recognized entity: %s, category: %s, subcategory: %s, confidence score: %f.%n",
                        entity.getText(), entity.getCategory(), entity.getSubcategory(), entity.getConfidenceScore()));


    }
}

