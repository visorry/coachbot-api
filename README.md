# Notes API

## Description

Notes API is a platform for storing and sharing notes. It allows users to create, retrieve, update, and delete notes of various types, including text, audio, and video. Users can also share their notes with other users.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/visorry/coachbots-assignment.git

Navigate to the project directory:
   ```shell
cd notes
```
Set up a virtual environment (optional but recommended):
python -m venv venv


Activate the virtual environment:

For Windows:
venv\Scripts\activate

For Unix/Linux:
source venv/bin/activate

Install the project dependencies:
pip install -r requirements.txt

Apply database migrations:
python manage.py migrate

Start the development server:
python manage.py runserver


Access the API at http://localhost:8000/api/notes/

## API Endpoints

GET /api/notes/: Retrieve a list of all notes.

POST /api/notes/: Create a new note.

GET /api/notes/{id}/: Retrieve a specific note by its ID.

PUT /api/notes/{id}/: Update a specific note by its ID.

DELETE /api/notes/{id}/: Delete a specific note by its ID.




## Usage

To create a new note, send a POST request to /api/notes/ with the required fields in the request body.

To retrieve a list of all notes, send a GET request to /api/notes/.

To retrieve a specific note, send a GET request to /api/notes/{id}/, where {id} is the ID of the note.

To update a specific note, send a PUT request to /api/notes/{id}/ with the updated fields in the request body.

To delete a specific note, send a DELETE request to /api/notes/{id}/.



Configuration

The project uses SQLite as the default database. You can change the database settings in the project's settings.py file.
You can modify the note types by editing the NOTE_TYPES constant in the Note model.

License
This project is licensed under the MIT License.

Authors

Special thanks to the Django and Django Rest Framework communities for their fantastic tools and documentation.
