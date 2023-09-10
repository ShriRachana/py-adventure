# Client : 
    - Java or Python is used 
    - Desired Capabilities : Androind or iOS
    - Actions : click, sendkeys, tap, swipe, scroll 
# Appium : 
    - Appium server that has Node JS 
    - Enable REST API Calls
# Server : 
    - Android, google, Androind Studio
        - Instruments, UI Automator, UI Automator2
    - iOS, Apple, Xcode, 
        - UI Automation, XCUITest

# Communication :
    - from the client API calls are sent to the Appium server i.e with REST API also called HTTP Methods
    Example HTTP Methods : GET, PUT, POST, DELETE
    - Request sent from say Android 8.0 client server to Appium on the machine (Local/host). Appium is started on the machine, from the Appium server it is sent to the Server that has the android/iOS frameworks like UIAutomator2 or XCUITest. 
    - UIAutomator will perform tests on the real android device. 
    - Example 2 : Request is sent for iOS from the client server to Appium server then that Appium server will inturn send a request to XCUITest to execute/perfom test on the iOS device/simulator. 
    -- These frameworks like UIAutomator and XCUITest interact with the real device and not the appium directly. 
    -- Library is coming from the selenium part on the client in (Java, Python, C#, Javascript) from functions and classes and then it is sent as HTTP Request to Appium server
    