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
5. Run `pytest` and that\'s it! Watch the results right in the console

---

### Frontend