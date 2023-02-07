# Google Cloud Functions Course
## Starting a new project
To start a new project in Google Cloud , we can go to
[Firebase Console](https://console.firebase.google.com) or create it from the
[Google Cloud Platform Console](https://console.cloud.google.com).

Postman,for testing APIs, can be downloaded through this [link](https://www.postman.com/downloads/).

Basic CRUD operations in firestore are available in this [video](https://www.youtube.com/watch?v=N0j6Fe2vAK4&t=1331s) and in this Github [link](https://github.com/sri-harsha97/firestoretutorial).
## Creating a Virtual Environment
First we have to install `python3-venv` with the following command:
```commandline
sudo apt install python3-venv
```
Then we execute following command
```
python3 -m venv venv 
```
To activate Virtual Enivronment
```
source venv/bin/activate
```
To add new packages 
```
 pip install -r Requirements.txt
```

## Downloading Google Cloud SDK 

To install the Google Cloud SDK, all of the instructions are [here](https://cloud.google.com/sdk/docs/downloads-versioned-archives). Commands are also given below.If required, follow this [video](https://www.youtube.com/watch?v=k-8qFh8EfFA).

Move the downloaded SDK to the root directory 
```
mv google-cloud-cli-417.0.0-darwin-x86.tar.gz ~/
```
Terminal to the root directory and extract
```commandline
tar xopf google-cloud-cli-417.0.0-darwin-x86.tar.gz
```
Install SDK
```commandline
./google-cloud-sdk/install.sh
```
Initialize the gcloud CLI to login and setup the appropriate project
```commandline
./google-cloud-sdk/bin/gcloud init
```


## Running cloud function in the local environment
```commandline
functions-framework --target [function_name] --debug 
```


## Deploying your function
Setting up the project ID
```commandline
gcloud config set project [yourproject_ID]
```
Deploying function
```commandline
 gcloud functions deploy [function_name] --runtime python37 --trigger-http
```
