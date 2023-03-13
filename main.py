# Importing the GmailApi class from the module google_api
from google_api import GmailApi

if __name__ == "__main__":
    # Created instance to then call the methods
    api = GmailApi(token_file="token.json")

    """
    Calls the search_emails() method of the api instance with the parameters user_id="me", 
    search_query="python", and activate=True. This method searches for emails with the 
    specified search query and returns a list of the messages that match. The activate 
    parameter determines whether or not the method is executed.
    """
    message_search = api.search_emails(user_id="me",
                                       search_query="python",
                                       activate=True)
    print(message_search)

    """
    Calls the send_email() method of the api instance with the parameters 
    to, from_, subject, message_content, and activate=False. This method sends 
    an email to the specified recipient with the specified subject and message content. 
    The activate parameter determines whether or not he method is executed.
    """
    send_email = api.send_email(to="pythonchallenge.sisco@gmail.com",
                                from_="pythonchallenge.sisco@gmail.com",
                                subject="This is an email to test the python script",
                                message_content="Test 3",
                                activate=False)