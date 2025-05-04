package detectLanguage;

import com.azure.ai.textanalytics.TextAnalyticsAsyncClient;
import com.azure.ai.textanalytics.TextAnalyticsClient;
import com.azure.ai.textanalytics.TextAnalyticsClientBuilder;
import com.azure.ai.textanalytics.models.DetectedLanguage;
import com.azure.core.credential.AzureKeyCredential;
/*
Refer https://learn.microsoft.com/en-us/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-stable#analyze-sentiment
 */
public class DetectLanguage {

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
        TextAnalyticsAsyncClient textAnalyticsAsyncClient = new TextAnalyticsClientBuilder()
                .credential(new AzureKeyCredential(key))
                .endpoint(endpoint)
                .buildAsyncClient();

        System.out.println("************************\n" );

        String document1 = "Bonjour tout le monde";
        System.out.println(document1);
        DetectedLanguage detectedLanguage1 = textAnalyticsClient.detectLanguage(document1);
        System.out.printf("Detected language name: %s, ISO 6391 name: %s, confidence score: %f.%n",
                detectedLanguage1.getName(), detectedLanguage1.getIso6391Name(), detectedLanguage1.getConfidenceScore());

        System.out.println("************************\n" );

        String document2 = "enthokke undu vishesham";
        System.out.println(document2);
        DetectedLanguage detectedLanguage2 = textAnalyticsClient.detectLanguage(document2);
        System.out.printf("Detected language name: %s, ISO 6391 name: %s, confidence score: %f.%n",
                detectedLanguage2.getName(), detectedLanguage2.getIso6391Name(), detectedLanguage2.getConfidenceScore());

        System.out.println("************************\n" );

        String document3 = "tumhara naam kya hai?";
        System.out.println(document3);
        DetectedLanguage detectedLanguage3 = textAnalyticsAsyncClient.detectLanguage(document3).block(); // Purposeful block to adapt to blocking call
        System.out.printf("Detected language name: %s, ISO 6391 name: %s, confidence score: %f.%n",
                detectedLanguage3.getName(), detectedLanguage3.getIso6391Name(), detectedLanguage3.getConfidenceScore());


    }
}
