import email
import os
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage

# If modifying these scopes, delete the file token.json
SCOPES = ['https://mail.google.com/']


class GmailApi:
    def __init__(self, token_file=str()):
        self.token_file = token_file

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

    def send_email(self,
                   to=str(),
                   from_=str(),
                   subject=str(),
                   message_content=str()):

        service = self.service()

        # added this condition to avoid sending email when token.json file is not available
        if service is not None:
            try:
                message = EmailMessage()

                message.set_content(message_content)

                message['To'] = to
                message['From'] = from_
                message['Subject'] = subject

                # encoded message
                encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
                    .decode()

                create_message = {
                    'raw': encoded_message
                }
                # pylint: disable=E1101
                send_message = (service.users().messages().send
                                (userId="me", body=create_message).execute())
                print(f'Message Id: {send_message["id"]}')
            except HttpError as error:
                print(f'An error occurred: {error}')
                send_message = None
            return send_message
        else:
            print("token.json was not avialable and It was created because this is the first run, run the script "
                  "again to send"
                  "the email")

    # search_emails will return a list of message id's
    def search_emails(self, user_id=str(), search_query=str()):
        service = self.service()

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
