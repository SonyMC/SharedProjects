package imageAnalysisExtractTextFromImage;

import java.io.IOException;
import com.azure.ai.vision.imageanalysis.ImageAnalysisClient;
import com.azure.ai.vision.imageanalysis.ImageAnalysisClientBuilder;
import com.azure.core.credential.KeyCredential;


import com.azure.ai.vision.imageanalysis.models.DetectedTextLine;
import com.azure.ai.vision.imageanalysis.models.DetectedTextWord;
import com.azure.ai.vision.imageanalysis.models.ImageAnalysisResult;
import com.azure.ai.vision.imageanalysis.models.VisualFeatures;
import com.azure.core.util.BinaryData;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;

public class imageAnalysisExtractTextFromImage {

    /*
    Note : Create computer vision instance before running this and update the key and endpoint
    */

    private static  final String endpoint = "https://xxxx.cognitiveservices.azure.com/";
    private static  final String key = "xxxx";



    public static void main(String[] args) throws IOException {


        // Current Working Directory
        String cwd = System.getProperty("user.dir");

        // Local Image Path
        String source1 = "analyzeImage/src/main/resources/sample.jpg";
        String source2 = "analyzeImage/src/main/resources/church.jpg";
        String source3 = "analyzeImage/src/main/resources/handwritten.jpg";

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
        extractTextFromLocalImage(client, cwd, source1); // Local Image

        System.out.println("**********************");
        extractTextFromLocalImage(client, cwd, source3); // Local Image


        System.out.println("**********************");
        extractTextFromUrl(client, imageUrl); // Image url

    }

    private static void extractTextFromLocalImage(ImageAnalysisClient client, String cwd, String source) throws IOException {
        ImageAnalysisResult result = client.analyze(
                BinaryData.fromBytes(Files.readAllBytes(Paths.get(cwd, source))),
                Arrays.asList(VisualFeatures.READ), // visualFeatures
                null); // options: There are no options for READ visual feature

        // Print analysis results to the console
        System.out.println("Image analysis results:");
        System.out.println(" Read:");
        for (DetectedTextLine line : result.getRead().getBlocks().get(0).getLines()) {
            System.out.println("   Line: '" + line.getText()
                    + "', Bounding polygon " + line.getBoundingPolygon());
            for (DetectedTextWord word : line.getWords()) {
                System.out.println("     Word: '" + word.getText()
                        + "', Bounding polygon " + word.getBoundingPolygon()
                        + ", Confidence " + String.format("%.4f", word.getConfidence()));
            }
        }
    }


    private static void extractTextFromUrl(ImageAnalysisClient client, String imageUrl) throws IOException {
        ImageAnalysisResult result = client.analyzeFromUrl(
                imageUrl, //// imageUrl: the URL of the image to analyze
                Arrays.asList(VisualFeatures.READ), // visualFeatures
                null); // options: There are no options for READ visual feature

        // Print analysis results to the console
        System.out.println("Image analysis results:");
        System.out.println(" Read:");
        for (DetectedTextLine line : result.getRead().getBlocks().get(0).getLines()) {
            System.out.println("   Line: '" + line.getText()
                    + "', Bounding polygon " + line.getBoundingPolygon());
            for (DetectedTextWord word : line.getWords()) {
                System.out.println("     Word: '" + word.getText()
                        + "', Bounding polygon " + word.getBoundingPolygon()
                        + ", Confidence " + String.format("%.4f", word.getConfidence()));
            }
        }
    }
}
