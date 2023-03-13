# Google API Challenge

## Setup the project
- Clone this repo

## Install Dependencies
<code>make install env</code>

and then 

<code>make dependencies</code>

Be sure the python interpreter is all set for this project.

## GCP Credentials Setup

For the purposes of this challenge I went for the quickstart (check the [docs](https://developers.google.com/gmail/api/quickstart/python#set_up_your_environment)) approach regarding authentication, a credential.json has 
to be set in the project's root folder; in the email I provided the required json file in a secured way.


### In case you want to use your own credentials:
- [create](https://developers.google.com/gmail/api/quickstart/python#enable_the_api)
the gmail api key and then [authorize](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application) 
the crendentials.
- One last step here is to add a test user to the **OAuth consent screen**, this is because when you run the script for the first time you will need to add the user that you will uses to test the script.
Note: the email account used for this challenge is already added.