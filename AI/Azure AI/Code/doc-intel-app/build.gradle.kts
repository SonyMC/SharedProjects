plugins {
       java
       application
   }
   application {
       mainClass.set("DocIntelligence")
   }
   repositories {
       mavenCentral()
   }
   dependencies {
       implementation("com.azure:azure-ai-documentintelligence:1.0.0-beta.1")

   }