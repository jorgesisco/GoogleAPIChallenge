# Google API Challenge
As requested by the company, this project was built to set up GCP's Gmail API to handle specific requests.


## Features
- Send emails using python
- Search for emails based on a text query


## Getting Started

### Requirements
- Python 3.8 or higher
- Pipenv (optional, but recommended for managing dependencies)

### 1. Installing Required Dependencies
- [Clone the repository](https://github.com/jorgesisco/GoogleAPIChallenge)
- Navigate to the project folder
    ```
    cd GoogleAPIChallenge
    ```
- (Optional) If you're using Pipenv, create a virtual environment and install dependencies.

  ```
    make run
   ```
    it will install pipenv witht the dependencies from the requirement.txt

Be sure the python virtual environment is set for this project.

### 2. GCP Credentials Setup

For this challenge, I went for the quickstart approach (check the [docs](https://developers.google.com/gmail/api/quickstart/python#set_up_your_environment)) regarding authentication, and a ```credential.json``` has 
to be set in the project's root folder; I sent the required ```crendentials.json``` file in the email along with the test Gmail account credentials.


#### In case you want to use your own credentials:
- [Create](https://developers.google.com/gmail/api/quickstart/python#enable_the_api)
the gmail api key and then [authorize](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application) 
the crendentials.
- One last step here is to add a test user to the **OAuth consent screen**, this is because when you run the script for the first time you will need to login with the user that you will use to test the script.

**Note:** The email account created to set the API for this challenge is already added as a test user.

### 3. Running the application
To run the application, execute the following command from the project's root:

```
python main.py
```

Also you can run the main.py file from the IDE.

**Note:** Check the each method's parameter active to be set to ```True``` in order to execute sending the email or search for emails.


## Approach for the Challenge
- The main.py file creates the instance of the class GmailApi with the ```token.json``` path as a parameter


- Inside the ```GmailApi``` we have five methods:

  - ```Constructor method``` to initialize the instance's attribute created for the class.
  - ```service()``` Creates the service to access the Gmail API; it checks if the token.json file exists. If not, It will prompt the user to log in to the Gmail of the designated test user in the GCP console.
  - ```send_email()``` Taking the parameters to(receiver), from_(sender), subject, message_content, activate=True, to then send an email
  - ```search_emails``` Takes the parameter user_id, search_query, activate=True. This will search for emails based on a given query and return the results of that search in the output, and a txt file, [search operators](https://support.google.com/mail/answer/7190?hl=en) can also be used in the ```search_query``` parameter.
  - ```get_messages``` This helper function is used inside ```search_emails()``` to handle email ids, find the message's content, and decode each one.

##  Considerations
The challenge was based on the provided scope by the recruiter, building a script to handle sending emails and searching for emails based on a query.
Something that could be implemented here is a rest API using FastApi to handle the script with HTTP requests.