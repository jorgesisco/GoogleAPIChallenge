from google_api import GmailApi


if __name__ == "__main__":
    if __name__ == "__main__":
        api = GmailApi(token_file="token.json")

        #This will return a list of messages, and also create a text file which each message
        message_search = api.search_emails(user_id="me", search_query="python")
        print(message_search)

        # api.send_email(to="pythonchallenge.sisco@gmail.com",
        #                from_="pythonchallenge.sisco@gmail.com",
        #                subject="Invitation to Attend a Team Meeting",
        #                message_content="I hope this email finds you in good health and spirits.")
