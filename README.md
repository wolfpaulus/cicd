# ERAU CS 399 
## CI/CD
### Status ..

CI is a software development practice in which incremental code changes are made frequently and reliably. 
Automated build-and-test steps triggered by CI ensure that code changes being merged into the repository are reliable. 
The code is then delivered quickly and seamlessly as a part of the CD process.

## Objectives
Learn how continuous integration and deployment (CI/CD) allows professional teams to make dozens of changes while 
making sure everyone is coordinated and nothing is broken. 

Create a complete CI/CD pipeline and experience how pushing code into a source code repository triggers tests to be 
performed, a container to be built, tested, and its image published into a registry, the image to be pulled from a 
container server and bringing your web application to life.

## Prerequisites
It's not necessary to build and run docker images on your local machine. 
However, if you want to do so, you need to install docker on your local machine.
On a Mac, you can install docker desktop from https://www.docker.com/products/docker-desktop
On a Windows machine, you can install docker desktop from https://www.docker.com/products/docker-desktop
On a Linux machine, you can install docker from https://docs.docker.com/engine/install/
Again, it's not necessary to install docker on your local machine, up to you ...

## Fork this repository
Login to you github account and search for this repo: **wolfpaulus/cicd** .. cick on it.

**_Fork_** this repo to your own github account.
You can do this by clicking on the "Fork" button in the upper right corner of this page.
Keep the Repo name as is, i.e. ```cicd``` and copy the main branch to your own repo. I.e., click on the green 
"Create fork" button.

### PAT (Personal Access Token)
Open your account settings (not this repo's settings). 
Open Developer settings (bottom of the left menu).
Open Personal Access Tokens
Open Tokens (classic)
- Generate a new Token (classic)
- Provide a name, e.g. CICD
- Reasonable expiration 
  - Check: 
    - repo
    - workflow
    - write:package
    - delete:packages
    - read:org
    - gist
    
  Copy your personal access token now. You won’t be able to see it again!

### GitHub Secrets
This time open the forked ```cicd``` repo's settings (not your account settings)
- Under Security, open Secrets and variables
  - Actions
    - Secret
      - Click "New repository secret"
        - Add a new secret
          - Name: **REPO_GHA_PAT**
          - Value: <your_personal_access_token>
            - Click Add secret  


# Pull the repo to your local machine
Open PyCharm, if it opens an existing project, close the project.
On the welcome screen, click on "Get from VCS" and provide the URL to your forked repo. E.g.:
```https://github.com/<Your User Name>/cicd```
Click on "Clone" and wait for the project to be cloned.
 
Make a small change to the README.md file, e.g. remove the two badges at the top. 
Those refer to the original repo and will not work for your forked repo anyway. 
```
[![run...]]
[![docker...]]
```
Right click on the README.md file and select "Git -> commit" .
Provide a commit msg, e.g. remove badges, and click the "Commit and Push..." button.
Provide your github user name and email address and click "OK".
Eventually you will be asked for your github credentials. Provide your token you created above.

## GitHub Actions
Open your forked repo on github.com and verify that your changes have been pushed.
Open the Actions tab in your forked repo.
Click the green "I understand my workflows..." button.

Make another small change to the README.md file, e.g. add a new line at the top and push the change to github.
Return to the Actions tab in your forked repo and verify that the tests are run and the docker image is built.

# Details
This project is a simple web application that displays if a given number is odd or even.
The application is written in Python and uses python's http.server, not adding additional requirements.

Unit tests are written using pytest. I.e., **pytest** needs to be installed to run the tests.

Two **github actions** are defined to run the tests and build the docker image.
The docker image is run and tested before pushed to the **github container registry**.

From there the image can pulled and deployed automatically, 
for instance by running [Watchtower](https://containrrr.dev/watchtower/) on the server.

## Testing locally
To run the tests locally, you need to install pytest and set the PYTHONPATH environment variable to the src directory.
The following steps show how to do this in a virtual environment:
Activate the virtual environment, e.g. 
```source ./venv/bin/activate```

```pip install pytest```

Set the environment variable PYTHONPATH to the src directory, e.g. 
```export PYTHONPATH=./src```

Run the tests, e.g. 
```python3 -m pytest  or simply pytest```

## Running the application locally
Open a terminal, navigate to the project directory (```./cicd```) and run the following commands:

```python3 ./src/ws.py```

Now open a browser and navigate to http://localhost:8000/ and enter a number to see if it is odd or even.

## Running the application in a container locally
To run the application in a container, you need to have docker installed.
Open a terminal, navigate to the project directory (```./cicd```) and run the following commands:

```docker build -t odd-even .```

```docker run -p 8080:8080 odd-even```

Now open a browser and navigate to http://localhost:8080/ and enter a number to see if it is odd or even.

## Testing the application in a container locally 
To run the tests in a container, you need to have docker installed.
Open a terminal, navigate to the project directory (```./cicd```) and run the following commands:

```docker build -t odd-even .```

```docker run odd-even /cicd/healthcheck.sh```

The script will exit with 0 "Health check was OK 200" if the tests pass and 1 if they fail.


## Triggering the workflows
You can either push a new commit to the repo or manually trigger the workflows.
To manually trigger a workflow, open the Actions tab, click on a workflow under "All workflows".
Click on the "Job" on the left side of the screen and click the "Run workflow" button.
