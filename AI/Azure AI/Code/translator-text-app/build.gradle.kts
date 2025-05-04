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