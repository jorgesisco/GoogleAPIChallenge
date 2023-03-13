from google_api import GmailApi

if __name__ == "__main__":
    api = GmailApi(token_file="token.json")

    # This will return a list of emails based on the used search query, and also create a text file which a message
    # per line
    message_search = api.search_emails(user_id="me",
                                       search_query="Meeting",
                                       activate=True)  # Set active parameter to True
    print(message_search)

    send_email = api.send_email(to="pythonchallenge.sisco@gmail.com",
                                from_="pythonchallenge.sisco@gmail.com",
                                subject="This is an email to test the python script",
                                message_content="Test 3",
                                activate=False)  # Set active parameter to True
