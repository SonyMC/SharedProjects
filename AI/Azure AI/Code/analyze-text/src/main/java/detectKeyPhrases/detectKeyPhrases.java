package detectKeyPhrases;

import com.azure.ai.textanalytics.TextAnalyticsAsyncClient;
import com.azure.ai.textanalytics.TextAnalyticsClient;
import com.azure.ai.textanalytics.TextAnalyticsClientBuilder;
import com.azure.core.credential.AzureKeyCredential;
/*
Refer https://learn.microsoft.com/en-us/java/api/overview/azure/ai-textanalytics-readme?view=azure-java-stable#analyze-sentiment
 */
public class detectKeyPhrases {


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

        String document1 = "My cat might need to see a veterinarian.";
        System.out.println(document1);
        System.out.println("Extracted phrases:");
        textAnalyticsClient.extractKeyPhrases(document1).forEach(keyPhrase -> System.out.printf("%s.%n", keyPhrase));

        System.out.println("************************\n" );

        String document2 = "The car hit Tom at 2.30 p.m. yesterday";
        System.out.println(document2);
        System.out.println("Extracted phrases:");
        textAnalyticsClient.extractKeyPhrases(document2).forEach(keyPhrase -> System.out.printf("%s.%n", keyPhrase));

    }





}
