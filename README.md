This is a project that creates an API integrating with Pipefy. For this, the Python language and the FastApi framework were used in the backend integrated with Pipefy's Graphql. In the frontend, a project was created using the Django framework. An architecture based on SOLID in layers was adopted. After downloading, it is suggested to create a virtualized environment and install the necessary packages. Follow the steps

1-Install Python
https://www.python.org/downloads/

2 Create a virtualized environment for each project
- after downloading the project, access the app folder where the backend is and install the virtualized environment by running the command:
- python3 -m venv environment_name
- run the virtualized environment
- run pip install -r requirements.txt
3 Access the pipefy frontend folder
- install the virtualized environment
- python3 -m venv environment_name
- run pip install -r requirements.txt

4 Run each virtualized environment
enter the \app folder in the same folder where the main.py file is and run the command:
- uvicorn main:app --host 127.0.0.1 --port 8080 (change to your preferred port)

5 Enter the pipefy folder which is the frontend
- in the same folder where the manage.py file is, run the command:
python .\manage.py runserver

6 In the backend, access the app\integration\access.py folder and place the token generated in the Pipefy portal so that you can access your pipes and cards
in the portal https://app.pipefy.com/
