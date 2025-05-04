package sentimentAnalysis;

import com.azure.ai.textanalytics.TextAnalyticsAsyncClient;
import com.azure.ai.textanalytics.TextAnalyticsClient;
import com.azure.ai.textanalytics.TextAnalyticsClientBuilder;
import com.azure.ai.textanalytics.models.DocumentSentiment;
import com.azure.core.credential.AzureKeyCredential;
// Refer: https://learn.microsoft.com/en-us/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-stable#analyze-sentiment
public class SentimentAnalysis {
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

        String document1 = "The hotel was dark and unclean. I like microsoft.";
        System.out.println(document1);
        DocumentSentiment documentSentiment1 = textAnalyticsClient.analyzeSentiment(document1);
        System.out.printf("Analyzed document sentiment: %s.%n", documentSentiment1.getSentiment());
        documentSentiment1.getSentences().forEach(sentenceSentiment ->
                System.out.printf("Analyzed sentence sentiment: %s.%n", sentenceSentiment.getSentiment()));

        System.out.println("************************\n" );

        String document2 = "John the Ripper struck terror in the hearts of the citizens of London";
        System.out.println(document2);
        DocumentSentiment documentSentiment2 = textAnalyticsAsyncClient.analyzeSentiment(document2).block(); // Purposeful block to adapt to blocking call
        System.out.printf("Analyzed document sentiment: %s.%n", documentSentiment2.getSentiment());
        documentSentiment2.getSentences().forEach(sentenceSentiment ->
                System.out.printf("Analyzed sentence sentiment: %s.%n", sentenceSentiment.getSentiment()));
    }
}
