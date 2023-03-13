# Google API Challenge

## Setup the project
- Clone this repo

## 1. Install Dependencies

In the project's folder, open temrinal and type:

<code>make install env</code>

and then 

<code>make dependencies</code>

Be sure the python interpreter is all set for this project.

## 2. GCP Credentials Setup

For the purposes of this challenge I went for the quickstart (check the [docs](https://developers.google.com/gmail/api/quickstart/python#set_up_your_environment)) approach regarding authentication, a credential.json has 
to be set in the project's root folder; in the email I sent the required json file can be found.


### - In case you want to use your own credentials:
- [create](https://developers.google.com/gmail/api/quickstart/python#enable_the_api)
the gmail api key and then [authorize](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application) 
the crendentials.
- One last step here is to add a test user to the **OAuth consent screen**, this is because when you run the script for the first time you will need to add the user that you will uses to test the script.

**Note:** The email account used for this challenge is already added as a test user.

# 3. Approach for the Challenge
- The main.py file creates the instance of the class GmailApi with the ```token.json``` path as a parameter


- Inside the ```GmailApi``` we have five methods:

  - ```Constructor method``` to initialize the instance's attribute created for the class.
  - ```service()``` Creates the service to access the Gmail API, it checks if the token.json file exists, if not It will prompt the user to log in to the gmail of to the designated test user in the GCP console.
  - ```send_email()``` Taking the parameters to(receiver), from_(sender), subject, message_content, activate=True, to then send an email
  - ```search_emails``` Takes the parameter user_id, search_query, activate=True, This will search for emails based on a given query and will return the results of that search in the output and in a txt file, [search operators](https://support.google.com/mail/answer/7190?hl=en) can also be used in the query.
  - ```get_messages``` This a helper function used inside ```search_emails()``` to handle email ids to then find the message's content and decode each one.

