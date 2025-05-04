package imageAnalysisGenerateCaption;

import com.azure.ai.vision.imageanalysis.ImageAnalysisClient;
import com.azure.ai.vision.imageanalysis.ImageAnalysisClientBuilder;
import com.azure.core.credential.KeyCredential;

import com.azure.ai.vision.imageanalysis.models.ImageAnalysisOptions;
import com.azure.ai.vision.imageanalysis.models.ImageAnalysisResult;
import com.azure.ai.vision.imageanalysis.models.VisualFeatures;
import com.azure.core.util.BinaryData;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
public class imageAnalysisGenerateCaption {

    /*
    Note : Create compute vision instance before running this and update the key and endpoint
    */

    private static  final String endpoint = "https://xxxx.cognitiveservices.azure.com/";
    private static  final String key = "xxxx";



    public static void main(String[] args) throws IOException {

        // Current Working Directory
        String cwd = System.getProperty("user.dir");

        // Local Image Path
        String source1 = "analyzeImage/src/main/resources/sample.jpg";
        String source2 = "analyzeImage/src/main/resources/church.jpg";
        
        // Image url
        String imageUrl = "https://aka.ms/azsdk/image-analysis/sample.jpg";

        if (endpoint == null || key == null) {
            System.out.println("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'.");
            System.out.println("Set them before running this sample.");
            System.exit(1);
        }

        // Create a synchronous Image Analysis client.
        ImageAnalysisClient client = new ImageAnalysisClientBuilder()
                .endpoint(endpoint)
                .credential(new KeyCredential(key))
                .buildClient();


//    // Create an asynchronous Image Analysis client.
//    ImageAnalysisAsyncClient asyncClient = new ImageAnalysisClientBuilder()
//            .endpoint(endpoint)
//            .credential(new KeyCredential(key))
//            .buildAsyncClient();


        
        
        System.out.println("**********************");


        generateContentSummaryFromLocalImage(client, cwd, source1); // Local Image


        System.out.println("**********************");
        generateContentSummaryFromLocalImage(client, cwd, source2); // Local Image


        System.out.println("**********************");  //// Image url
        generateContentSummaryFromUrl(client, imageUrl);

    }

    private static void generateContentSummaryFromLocalImage(ImageAnalysisClient client, String cwd, String source) throws IOException {

                ImageAnalysisResult result =
                    client.analyze(
                      BinaryData.fromBytes(Files.readAllBytes(Paths.get(cwd, source))), // imageData: Image file loaded into memory as BinaryData
                      Arrays.asList(VisualFeatures.CAPTION), // visualFeatures
                      new ImageAnalysisOptions().setGenderNeutralCaption(true)); // options:  Set to 'true' or 'false' (relevant for CAPTION or DENSE_CAPTIONS visual features)
                     // Print analysis results to the console
                     System.out.println("Image analysis results:");
                     System.out.println(" Caption:");
                     System.out.println("   \"" + result.getCaption().getText() + "\", Confidence "
                    + String.format("%.4f", result.getCaption().getConfidence()));
               }

    private static void generateContentSummaryFromUrl(ImageAnalysisClient client, String url) throws IOException {

                ImageAnalysisResult result = client.analyzeFromUrl(
                        "https://aka.ms/azsdk/image-analysis/sample.jpg", // imageUrl: the URL of the image to analyze
                        Arrays.asList(VisualFeatures.CAPTION), // visualFeatures
                        new ImageAnalysisOptions().setGenderNeutralCaption(true)); // options:  Set to 'true' or 'false' (relevant for CAPTION or DENSE_CAPTIONS visual features)
                // Print analysis results to the console
                System.out.println("Image analysis results:");
                System.out.println(" Caption:");
                System.out.println("   \"" + result.getCaption().getText() + "\", Confidence "
                        + String.format("%.4f", result.getCaption().getConfidence()));


        }




}
