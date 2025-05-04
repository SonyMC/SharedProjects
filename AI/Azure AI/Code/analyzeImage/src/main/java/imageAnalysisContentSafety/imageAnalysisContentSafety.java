package imageAnalysisContentSafety;

import com.azure.ai.contentsafety.ContentSafetyClient;
import com.azure.ai.contentsafety.ContentSafetyClientBuilder;
import com.azure.ai.contentsafety.models.AnalyzeImageOptions;
import com.azure.ai.contentsafety.models.AnalyzeImageResult;
import com.azure.ai.contentsafety.models.ContentSafetyImageData;
import com.azure.ai.contentsafety.models.ImageCategoriesAnalysis;
import com.azure.ai.vision.imageanalysis.ImageAnalysisClient;
import com.azure.ai.vision.imageanalysis.models.DetectedTextLine;
import com.azure.ai.vision.imageanalysis.models.DetectedTextWord;
import com.azure.ai.vision.imageanalysis.models.ImageAnalysisResult;
import com.azure.ai.vision.imageanalysis.models.VisualFeatures;
import com.azure.core.credential.KeyCredential;
import com.azure.core.util.BinaryData;
import com.azure.core.util.Configuration;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

public class imageAnalysisContentSafety {
    /*
    Note : Create content instance before running this and update the key and endpoint
    */

    private static  final String endpoint = "https://xxxx.cognitiveservices.azure.com/";
    private static  final String key = "xxxx";


    public static void main(String[] args) throws IOException {
        // Current Working Directory
        String cwd = System.getProperty("user.dir");

        // Local Image Path
        String source = "analyzeImage/src/main/resources/women-violence.jpg";
        System.out.println("**********************");
        extractContentSafety(cwd, source);

        // Image url
        // String imageUrl = "https://aka.ms/azsdk/image-analysis/sample.jpg";

    }

    private static void extractContentSafety(String cwd, String source) throws IOException {
        ContentSafetyClient contentSafetyClient = new ContentSafetyClientBuilder()
                .credential(new KeyCredential(key))
                .endpoint(endpoint).buildClient();

        ContentSafetyImageData image = new ContentSafetyImageData();

        image.setContent(BinaryData.fromBytes(Files.readAllBytes(Paths.get(cwd, source))));


        AnalyzeImageResult response =
                contentSafetyClient.analyzeImage(new AnalyzeImageOptions(image));

        for (ImageCategoriesAnalysis result : response.getCategoriesAnalysis()) {
            System.out.println(result.getCategory() + " severity: " + result.getSeverity());
        }
    }



}
