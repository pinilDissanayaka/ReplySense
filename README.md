# Email Reply Automation
This project leverages GPT-4 to automatically generate email replies based on unread emails. It integrates with the Gmail API to fetch emails, and OpenAI's GPT-4 for generating context-aware replies. The application is built using Streamlit, which provides an interactive UI for users to generate and send email responses.

## Features
- Unread Email Fetching: Retrieves the latest unread emails from your Gmail inbox.
- Automated Reply Generation: Automatically generates professional email replies using GPT-4.
- Reply Customization: Users can edit the generated reply before sending.
- Email Sending: Send the generated reply directly from the app.
- Setup Instructions
  
1. Clone the Repository
First, clone this repository to your local machine:
```
git clone https://github.com/pinilDissanayaka/ReplySense.git
cd ReplySense
```

2. Install Dependencies
You need to install the required dependencies. Run the following command:
```
pip install -r requirements.txt
```

Alternatively, you can manually install the necessary packages:
```
pip install streamlit openai google-api-python-client google-auth-httplib2 google-auth-oauthlib langchain
```

3. Set Up Environment Variables
- Rename .env.example to .env and fill in your environment variables:
  - MY_EMAIL=<your-email-address>
  - OPENAI_API_KEY=<your-openai-api-key>

Example:
```
MY_EMAIL=your-email@gmail.com
OPENAI_API_KEY=your-openai-api-key
```

4. Download Google API Credentials
  i. Go to Google Cloud Console.
  ii. Create a new project and enable the Gmail API.
  iii. Download the OAuth 2.0 credentials as a credentials.json file.
  iv. Place the credentials.json file in the root of the project directory.

5. Run the Application
Once everything is set up, you can run the app using the following command:
```
streamlit run app.py
```

This will start the Streamlit web application, and you can open it in your browser.

6. Authentication
- The first time you run the app, it will ask you to authenticate with your Gmail account via a browser.
- Ensure your Gmail credentials are valid and allow the app access to read and send emails.
  
7. How to Use
- Once the app is running, it will display unread emails from your inbox.
- Click the "Generate Reply" button for an email to have GPT-4 generate a response.
- You can review and edit the generated reply.

## UI Images and Screenshots
![Screenshot 2024-11-22 224512](https://github.com/user-attachments/assets/64da159f-f414-42f8-93db-133639500375)
![Screenshot 2024-11-22 224455](https://github.com/user-attachments/assets/5d4ba6b0-beb1-4e81-89a4-aad5f1eeb7c8)

## Example Workflow
- Login and fetch emails: The app automatically connects to your Gmail account and fetches unread emails.
- Generate a reply: After selecting an email, click "Generate Reply" to generate an automated response using GPT-4.
- Review and edit: Check the reply, and edit if necessary.
- Send the reply: Once satisfied with the reply, send it with a click.


## Troubleshooting
- Error: "Failed to authenticate with Gmail API."
  - Make sure the credentials.json file is in the correct directory and that your Google Cloud project is set up correctly.
  - Ensure that your Gmail account has authorized the app to access your inbox.


## License
This project is licensed under the MIT License.

