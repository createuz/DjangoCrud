# Django CRUD

This is a simple Django project that demonstrates CRUD (Create, Read, Update, Delete) operations using Django's built-in
functionality.

### Features

- Create a person with name, company, email, and status
- List all people with their information
- Edit person's information
- Delete a person

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/createuz/crud.git
2. Navigate to the project directory:
   ```bash
   cd django-crud-example
3. Install the project dependencies:
   ```bash
   pip install -r requirements.txt
4. Apply the database migrations:
   ```bash
   python manage.py migrate
5. Start the development server:
   ```bash
   python manage.py runserver
6. Open your web browser and visit [localhost:8000](http://localhost:8000) to access the application.


### Usage
     - Click on the "Add Person" button to create a new person.
     - Fill in the required information and click "Save" to create the person.
     - The list of people will be displayed on the homepage.
     - Click on the person's name to view their details.
     - To edit a person's information, click on the "Edit" button next to their name.
     - To delete a person, click on the "Delete" button next to their name.

