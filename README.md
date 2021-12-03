# Tourist Guide Testing

Tourist Guide Testing serves to host all of the unit tests done on both the backend and the frontend parts of the application, alongisde the fully functional projects so the tests can be performed. Following is a brief description on how to run these tests for each core project submodule.

---

### Backend

In order to run the backend tests, you need to do the following:
1. Change directory into the root folder, named `backend` in our case
2. Create a new virtual environment with `python -m venv .venv`
3. Activate the environment, with slightly different commands depending on the platform
	- For macOS / *nix, run `.venv\bin\activate`
	- For Windows, run `.venv\Scripts\activate`
4. Install the required packages with `pip install -r requirements.txt`
5. Run `pytest` and that\'s it! Watch the test results and any errors right in the console

---

### Frontend

In order to run the frontend tests, you need to do the following:
1. Make sure you have the Selenium driver corresponding to your Chrome version installed. You can download it from [this link.](https://chromedriver.chromium.org/downloads)
2. Change directory to the test\'s root folder, which in our case is `TouristPageTest\src\test\java\mx\tec\lab`
3. Once installed, change the `webdriver.chrome.driver` system property in the `TouristPageTestApplicationTests.java` file to match your driver\'s file path in your system.
4. Use Maven (independently or through Spring Boot\'s included tools) to test your application with the following commands, in order:
	- `maven clean`
	- `maven install`
	- `maven test`
5. That\'s it! Watch the test results and any errors right in the console