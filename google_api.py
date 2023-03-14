import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import email
from email.message import EmailMessage

# If modifying these scopes, delete the file token.json
SCOPES = ['https://mail.google.com/']


class GmailApi:
    """
    This class is used to interact with the Gmail API; the constructor has token_file as a parameter.
    If the token file is unavailable, it will prompt the user to log in to the Gmail account. Keep in mind
    that the Gmail account most be listed in the test users in the OAuth consent screen in the GCP Console.
    """
    def __init__(self, token_file=str()):
        self.token_file = token_file

    """
    The service() method initializes the Gmail service and then returns the service object.
    
    All methods in the class depend on the service() method to initialize the Gmail API. 
    If the token_file parameter is not available, it will prompt the user to log in to the Gmail account; 
    in the next run, the method you decide to run first will work.
    """
    def service(self):
        creds = None
        if os.path.exists(self.token_file):
            creds = Credentials.from_authorized_user_file(self.token_file, SCOPES)
            service = build('gmail', 'v1', credentials=creds)
            return service

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.token_file, 'w') as token:
                token.write(creds.to_json())

            return None

    """
    The send_email() method takes the parameters to(receiver), from_(sender), subject, 
    message_content, active=True, to send an email using the Gmail API.
    """
    def send_email(self,
                   to=str(),
                   from_=str(),
                   subject=str(),
                   message_content=str(),
                   active=True):

        service = self.service()

        # Added this condition to avoid sending emails when token.json file is not available
        if service is not None and active is True:
            try:
                message = EmailMessage()

                message.set_content(message_content)

                message['To'] = to
                message['From'] = from_
                message['Subject'] = subject

                # Encoding the message
                encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                    .decode()

                create_message = {
                    'raw': encoded_message
                }

                send_message = (service.users().messages().send
                                (userId="me", body=create_message).execute())

                print(f'Message Id: {send_message["id"]}')

            except HttpError as error:
                print(f'An error occurred: {error}')
                send_message = None

            return send_message

        elif service is None:
            print("token.json was not available, and It was created because this is the first run; run the script "
                  "again to send."
                  "the email")
            return ""

        else:
            return ""

    """
    The search_emails() method searches for emails using a given search_query and returns 
    a list of message ids. It calls the get_messages method to fetch the actual message.
    """
    def search_emails(self, user_id=str(), search_query=str(), active=True):
        service = self.service()

        if service is not None and active is True:
            try:
                search_id = service.users().messages().list(userId=user_id, q=search_query).execute()
                results_number = search_id['resultSizeEstimate']

                if results_number > 0:
                    messages_id = search_id["messages"]
                    messages_id_list = [messageId['id'] for messageId in messages_id]

                    messages_texts = [self.get_messages(user_id=user_id, msg_id=i) for i in messages_id_list]

                    return messages_texts

                else:
                    print("No messages were found with this search query")
                    return ""

            except HttpError as error:
                print(f'An error occurred: {error}')
                return ""

        elif service is None:
            print("token.json was not available, and It was created because this is the first run; run the script "
                  "again to send."
                  "the email")
            return ""

        else:
            return ""

    """
    The get_messages() method retrieves the content of a message based on its id, decoded the message to plain text, 
    shows the messages as a list in the output and saves it to a file named messages.txt.
    """
    def get_messages(self, user_id, msg_id):
        service = self.service()
        try:
            message = service.users().messages().get(userId=user_id, id=msg_id, format="raw").execute()
            message_raw = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
            message_string = email.message_from_bytes(message_raw).get_payload()

            with open("messages.txt", "a") as file:
                file.write(message_string)

            return message_string

        except HttpError as error:
            print(f'An error occurred: {error}')

            return None
