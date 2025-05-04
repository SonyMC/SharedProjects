https://learn.microsoft.com/en-us/azure/ai-services/translator/quickstart-text-rest-api?tabs=java



1) Open powershell:


2) cmd: mkdir doc-intel-app; cd doc-intel-app

3) cmd: gradle init --type basic


4) When prompted to choose a DSL, select Kotlin

5) Accept the default project name (translator-text-app) by selecting Return or Enter


6) Update build.gradle.kts with the following code:
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

7) Create your application:
cmd: mkdir -p src/main/java


You should see the following directory structure as a result:
	- src
		- main 
			- java 

8) Navigate to the java directory and create a file named DocIntelligence.java



9)Open the DocIntelligence.java



10) Build and run your Java application

	- gradle build
	- gradle run


