# FlaskStructureGenerator

## Generate all necessary documents to start a new Flask project
Creating all the necessary documents to create a simple project and then proceed with development.

- The goal of the project was to create a quick and simple way to create new Flask projects.

- The idea is to evolve the project to create models, views and controllers files.

- But to begin with, the current project already solves a lot of pain! 

- It will create the entire structure, it will create a virtual environment with the name "env" (The same version of python installed on the system will be installed. If you want to create a specific environment, change line 212 of the file specifying the version in the command before executing) and it will install the "flask", "gunicorn" and "python-dotenv" libraries into this virtual environment (All libraries with the latest version).
- 
### I decided to leave the repository open because this solution could be useful for many, and anyone who wants to improve the project is welcome.

Commands:
```
# Run Scripts to build structure:
python flask_generate.py "NewProjectName"

# Access the project:
cd "NewProjectName"

# Activate the "env" environment  (Windows)
env\Scripts\activate.bat

# Activate the "env" environment  (Linux or Mac)
source env/bin/activate

# Running the project:
python run.py
```
Example:
![image](https://github.com/user-attachments/assets/13c1b463-c887-43cc-acdf-ad494b18da18)

Structure created:
![image](https://github.com/user-attachments/assets/101ecff8-4d8d-4bcb-b923-9dfb15c56984)

Running project:
![image](https://github.com/user-attachments/assets/d3cb89d0-2803-49ca-beb8-20887762d45f)

Homepage:
![image](https://github.com/user-attachments/assets/02c1c6a8-91eb-43b2-b992-812c6becff31)
