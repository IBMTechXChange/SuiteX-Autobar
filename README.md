# SuiteX-Autobar

SuiteX-Autobar is an AI-powered API designed to integrate with SuiteX, a comprehensive business suite aimed at enhancing team collaboration and productivity. This API supports smart scheduling, automated document management, and video conferencing through advanced AI insights.

## Features

- **Automated Meeting Links**: Generates meeting links based on user requests.
- **Document Management**: Creates or edits documents automatically.
- **Calendar Events**: Handles date-specific events and reminders.
- **Email Generation**: Creates and formats emails based on user needs.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- IBM WatsonX AI Foundation Models
- `python-dotenv`

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/IBMTechXChange/SuiteX-Autobar.git
   cd SuiteX-Autobar

   ```
2. **Create a virtual environment (optional but recommended):**

   ```bash
   python -m venv venv
   ```
3. **Activate the virtual environment:**

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```
4. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```
5. **Set up environment variables:**

   Create a `.env` file in the root directory of the project with the following content:

   ```env
   API_KEY=your_ibm_watson_api_key
   PROJECT_ID=your_ibm_watson_project_id
   ```

### Running the Application

Start the Flask application using:

```bash
python app.py
```

The application will run on `http://0.0.0.0:8000`.

### API Endpoints

- **POST /generate**

  **Request Body:**

  ```json
  {
    "question": "Your prompt here"
  }
  ```

  **Response:**

  ```json
  {
    "response": "Generated JSON response based on the prompt"
  }
  ```

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your proposed changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Contact

For any inquiries or support, please contact us at [https://github.com/IBMTechXChange](https://github.com/IBMTechXChange)
