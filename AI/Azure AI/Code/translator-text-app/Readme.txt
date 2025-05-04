https://learn.microsoft.com/en-us/azure/ai-services/translator/quickstart-text-rest-api?tabs=java

** Important: Create required resource instance under a resource group  
1) Open powershell:


2) cmd:  mkdir translator-text-app; cd translator-text-app

3) cmd: gradle init --type basic


4) When prompted to choose a DSL, select Kotlin

5) Accept the default project name (translator-text-app) by selecting Return or Enter


6) Update build.gradle.kts with the following code:
plugins {
  java
  application
}
application {
  mainClass.set("TranslatorText")
}
repositories {
  mavenCentral()
}
dependencies {
  implementation("com.squareup.okhttp3:okhttp:4.10.0")
  implementation("com.google.code.gson:gson:2.9.0")
}



7) Create your application:
cmd: mkdir -p src/main/java


You should see the following directory structure as a result:
	- src
		- main 
			- java 

8) Navigate to the java directory and create a file named TranslatorText.java.



9)Open the TranslatorText.java 



10) Build and run your Java application

	- gradle build
	- gradle run


