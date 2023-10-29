# README

This is a README file for the project.

## Introduction

This project is a Flask application that sends emails using Python.

## Installation

To install the project, follow these steps:

1. Clone the repository.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Set the environment variable `SENDER_PASS` with the sender's password. To do this, run the following command:

   ```bash
   export SENDER_PASS=<sender_password>
   ```

## Usage

To use the project, follow these steps:

1. Run the Flask app by executing `python app.py`.
2. Access the application in your web browser at `http://localhost:5000`.
3. Fill in the email and content fields in the form.
4. Click the "Submit" button to send the email.
5. Run the deployment script by executing `./deploy.sh`. This script will install the required dependencies by running `pip install -r requirements.txt` and then run the Flask app by executing `python app.py`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.