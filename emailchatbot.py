# Frequently Asked Questions (FAQ) Data
faq_data = {
    "What is Nalosolutions email service?": "Nalosolutions email service is a robust and secure platform for managing and sending emails efficiently, tailored for businesses.",
    "How do I set up my email account?": "To set up your email account, go to the email settings page, enter your account details, and configure the server settings provided by Nalosolutions.",
    "What are the supported protocols?": "Nalosolutions email service supports IMAP, SMTP, and POP3 for seamless email management.",
    "What is the maximum email attachment size?": "The maximum email attachment size is 25MB per email. For larger files, we recommend using cloud services like Google Drive or Dropbox.",
    "How do I reset my email password?": "To reset your email password, go to the Nalosolutions account settings, select 'Forgot Password,' and follow the instructions sent to your recovery email.",
    "How can I improve email security?": "We recommend enabling two-factor authentication (2FA), using strong passwords, and avoiding clicking on unknown links or attachments.",
    "Does the email service offer spam filtering?": "Yes, Nalosolutions email service has an advanced spam filtering system to block unwanted emails and protect your inbox.",
    "How do I contact customer support?": "You can contact our customer support via email at support@nalosolutions.com or call our helpline at +233 30 255 5555."
}

def chatbot():
    while True:
        user_input = input("You: ").strip().lower()
        
        # Search for an exact match or a related FAQ response
        response = None
        for question, answer in faq_data.items():
            if user_input in question.lower():
                response = answer
                break

        if response:
            print(f"Bot: {response}")
        else:
            print("Bot: I'm sorry, I couldn't find an answer to your question. Please contact our support team at support@nalosolutions.com for further assistance.")

if __name__ == "__main__":
    chatbot()
