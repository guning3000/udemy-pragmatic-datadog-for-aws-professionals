# 13 ⚡ Hands-on Simple android kotlin

![](../imgs/b1de57270d034bc786e43f7759043be7.png)

## Step 1

start simple app kotlin in Android Studio

## Step 2 run application

## Step 3 add button

`MainActivity.kt`

```kotlin
val myButton = findViewById<Button>(R.id.button) // or view.findViewById in Fragment

        myButton.setOnClickListener {
            // Handle button click here
            Toast.makeText(this, "Button clicked!", Toast.LENGTH_SHORT).show()

            // You can perform any action:
            // startActivity(Intent(this, OtherActivity::class.java))
            // update UI, etc.
        }
```

`activity_main.xml`
```xml

    <Button
        android:id="@+id/button"
        android:layout_width="124dp"
        android:layout_height="63dp"
        android:text="Button"
        tools:layout_editor_absoluteX="170dp"
        tools:layout_editor_absoluteY="205dp"
        tools:ignore="MissingConstraints" />

```

## Step 4 create Datadog RUM

add deps to `build.gradle.kts`

```
implementation("com.datadoghq:dd-sdk-android-rum:2.14.0")
    implementation("com.datadoghq:dd-sdk-android-trace:2.14.0")
    implementation("com.datadoghq:dd-sdk-android-core:2.14.0")
    implementation("com.datadoghq:dd-sdk-android-gradle-plugin:1.14.0")
```

`MainActivity.kt`

deps

```kotlin
import com.datadog.android.Datadog
import com.datadog.android.DatadogSite
import com.datadog.android.core.configuration.Configuration
import com.datadog.android.privacy.TrackingConsent.GRANTED
import com.datadog.android.rum.Rum
import com.datadog.android.rum.RumConfiguration
import com.datadog.android.rum.tracking.ActivityViewTrackingStrategy
import com.datadog.android.trace.Trace
import com.datadog.android.trace.TraceConfiguration
import io.opentracing.util.GlobalTracer
import com.datadog.android.trace.AndroidTracer
```

code

```kotlin
val applicationId = "appid"
        val clientToken = "clienttoken"

        val environmentName = "appdemo"
        val appVariantName = "appvar"

        val configuration = Configuration.Builder(
            clientToken = clientToken,
            env = environmentName,
            variant = appVariantName
        )
            .useSite(DatadogSite.US1)
            .build()
        Datadog.initialize(this, configuration, GRANTED)


        val rumConfiguration = RumConfiguration.Builder(applicationId)
            .trackUserInteractions()
            .setSessionSampleRate(100.0f)
            .trackLongTasks(250L)
            .build()
        Rum.enable(rumConfiguration)
```
