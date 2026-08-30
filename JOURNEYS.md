## J-1: App startup smoke
<!-- after: 2 -->
<!-- covers: app.bootstrap, app.launch, ui.health -->
<!-- tags: smoke -->
Open the app in a fresh local environment → install the project dependencies → start Streamlit → load the browser page → verify the main UI renders without configuration errors → confirm the primary button is visible and ready for interaction.

## J-2: First-time greeting flow
<!-- after: 2 -->
<!-- covers: app.greeting, ui.feedback, app.bootstrap -->
Load the app from a clean session → read the single-page layout → click the greeting button once → verify the page updates with the expected Hello World message → confirm the interface remains stable and the text is immediately visible to the user.

## J-3: Repeated interaction reliability
<!-- after: 2 -->
<!-- covers: app.greeting, ui.feedback, app.launch -->
Open the app and observe the initial blank or idle state → click the greeting button several times in sequence → watch the interface after each press → confirm the app continues to respond predictably without stale state, crashes, or hidden errors.

## J-4: Refresh and recovery check
<!-- after: 2 -->
<!-- covers: app.launch, ui.health, app.greeting -->
Start the app → trigger the Hello World action → refresh the browser tab → return to the app page → confirm the app restarts cleanly and the greeting interaction can be performed again without manual fixes or reinstallation.

## J-5: Clean environment validation
<!-- after: 2 -->
<!-- covers: app.bootstrap, app.launch, ui.health -->
Create a new virtual environment → install dependencies from the requirements file → launch the app from the project root → wait for the Streamlit server to come up → check the page in the browser → validate that startup is consistent and easy for a developer to reproduce.

## J-6: Interactive usability pass
<!-- after: 2 -->
<!-- covers: app.greeting, ui.feedback, app.launch -->
Open the application and scan the UI for the main call to action → read the visible label and button affordance → click it with the mouse → confirm the output matches the product expectation → complete the flow without extra navigation, error pages, or confusing intermediate states.

## J-7: Local demo walkthrough
<!-- after: 2 -->
<!-- covers: app.bootstrap, app.greeting, ui.feedback -->
Start from a freshly booted environment → walk through the app as a first-time user would → confirm the developer can launch it quickly → invoke the greeting action → explain the output to a reviewer → verify the application feels like a polished single-user demo rather than a brittle prototype.

## J-8: Readiness for extension
<!-- after: 2 -->
<!-- covers: app.bootstrap, app.greeting, app.launch -->
Open the app in a normal local workflow → confirm the project structure is understandable and minimal → perform the greeting interaction → note how the button-driven UI is the only behavior needed for the initial release → verify the app remains easy to extend if future features are added.

## J-9: End-to-end single-user demo
<!-- after: 2 -->
<!-- covers: app.bootstrap, app.launch, app.greeting, ui.feedback -->
Run the full local setup workflow from a clean shell → start the app → navigate to the displayed page → interact with the button multiple times across the session → verify the app consistently produces the expected Hello World output and remains user-friendly for the demo scenario.
