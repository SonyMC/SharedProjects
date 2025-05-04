package textModeration;

import com.azure.ai.contentsafety.ContentSafetyClient;
import com.azure.ai.contentsafety.ContentSafetyClientBuilder;
import com.azure.ai.contentsafety.models.AnalyzeTextOptions;
import com.azure.ai.contentsafety.models.AnalyzeTextResult;
import com.azure.ai.contentsafety.models.TextCategoriesAnalysis;
import com.azure.core.credential.KeyCredential;
import com.azure.core.util.Configuration;


/*
Note: Does not work
https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Cwindows&pivots=programming-language-java
 */
    /*
    Note : Create content safety  instance before running this and update the key and endpoint
    */
public class textModeration {
    // Refer: https://learn.microsoft.com/en-us/azure/ai-services/content-safety/quickstart-text?tabs=visual-studio%2Cwindows&pivots=programming-language-java
    private static final String key = "xxxx";
    private static final String endpoint = "https://xxxx.cognitiveservices.azure.com/";
    public static void main(String[] args) {


        ContentSafetyClient contentSafetyClient = new ContentSafetyClientBuilder()
                .credential(new KeyCredential(key))
                .endpoint(endpoint).buildClient();

        AnalyzeTextResult response = contentSafetyClient.analyzeText(new AnalyzeTextOptions("Integrity is doing the right thing when no one is watching. Even when doing the right thing is hard, it is important to do it."));

        for (TextCategoriesAnalysis result : response.getCategoriesAnalysis()) {
            System.out.println(result.getCategory() + " severity: " + result.getSeverity());
        }

    }
}
