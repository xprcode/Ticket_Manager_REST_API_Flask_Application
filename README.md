# Ticket Manager REST API Flask Application

This Flask web application serves as a ticket manager, allowing users to add new events and receive email confirmations upon adding new events. 

## Overview

The application provides RESTful APIs for managing events and user-event relationships. Users can add events to their list, and upon successful addition, receive email confirmations.

## Features

- **Login**: Getting JWT access token generated with help of Flask JWT (extended version). It allows to have access to application REST API features. 
- **Event Management**: After geting JWT token, users can add events to their list and view their existing events.
- **Email Confirmation**: Upon adding a new event, users receive email confirmations.
- **RESTful API**: The application provides a RESTful API for seamless integration with other services.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   ```
2. Create and activate a virtual environment::
            virtualenv env -p python3
            source env/Scripts/activate

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:

   - Create a `.env` file in the root directory.
   - Define the required environment variables such as `DATABASE_URL`, `FLASK_APP_SECRET`, `MAIL_USERNAME`, `MAIL_PASSWORD`, etc.

4. Run the application:

   ```bash
   flask run
   ```

5. Access the application in your browser at [http://localhost:5000/](http://localhost:5000/).

## API Endpoints

### Event Resource

- **POST /event/:user_id/:event_id**
  - Add an event to the user's list and send email confirmation.
  - Requires authentication.
  - Example Request Body:
    ```json
    {
        "user_id": 1,
        "event_id": 1
    }
    ```
  - Example Response:
    ```json
    {
        "message": "Participation recorded successfully"
    }
    ```

### User Event Resource

- **GET /user_event/:user_id**
  - Get all events associated with the user.
  - Requires authentication.
  - Example Response:
    ```json
    {
        "events": [
            {
                "event_name": "Event 1",
                "event_adress": "123 Main St",
                "event_date": "2024-03-15"
            },
            {
                "event_name": "Event 2",
                "event_adress": "456 Oak St",
                "event_date": "2024-03-20"
            }
        ]
    }
    ```

- **GET /user_event/:user_id/:event_id**
  - Get details of a particular event associated with the user.
  - Requires authentication.
  - Example Response:
    ```json
    {
        "event": {
            "event_name": "Event 1",
            "event_adress": "123 Main St",
            "event_date": "2024-03-15"
        }
    }
    ```

## Database Models

- **User**: Represents a user of the application.
- **Events**: Represents an event.
- **EventParticipation**: Represents the relationship between users and events.

## Email Manager

The email manager module handles sending email notifications upon adding new events. It integrates with the application to provide seamless communication with users.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
