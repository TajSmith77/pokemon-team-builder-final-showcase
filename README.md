# Pokemon Team Builder App

Welcome to the Pokemon Team Builder App! This web application allows users to create, manage, and export Pokemon teams for use in Pokemon Showdown. Below is an overview of the app's functionality and features.

## Features

### User Management
- **Register:** Users can register for an account to access the app's features.
- **Login:** Registered users can log in to their accounts securely.
- **Edit Profile:** Users can edit their profile details, such as username and password.
- **Delete Account:** Users have the option to delete their account if needed.

### Pokemon Database
- **All Pokemon Page:** Browse through a comprehensive list of Pokemon with pagination, filtering, and searching capabilities.
- **Pokemon Details:** View detailed information about each Pokemon, including typing, abilities, stats, and moves.
- **Move Details:** Explore information about each move, such as type, power, accuracy, and PP.

### Team Management
- **Teams Page:** View a list of all user-created teams with pagination.
- **Create Team:** Create a new team by selecting six Pokemon, assigning abilities, and choosing moves.
- **Team Details:** Access detailed information about each team, including Pokemon lineup, abilities, and moves.
- **Edit Team:** Modify existing teams by adding, removing, or updating Pokemon, abilities, and moves.
- **Delete Team:** Delete unwanted teams from the user's profile.
- **Export Team:** Export teams as CSV, JSON, or TXT files for importing into Pokemon Showdown.

## Getting Started

To get started with the Pokemon Team Builder App, follow these steps:

1. **Clone Repository:** Clone this repository to your local machine.
2. **Install Dependencies:** Install the necessary dependencies by running `pip install -r requirements.txt`.
3. **Set Up Database:** Set up the database by running `python manage.py migrate`.
4. **Run Server:** Start the Django development server by running `python manage.py runserver`.
5. **Access App:** Access the app in your web browser at `http://localhost:8000`.

## Technologies Used

- **Django:** Backend framework for building the web application.
- **HTML/CSS/JavaScript:** Frontend technologies for creating the user interface.
- **Bootstrap:** Frontend framework for responsive design and styling.
- **AWS Elastic Beanstalk:** Deployment platform for hosting the application.
- **AWS RDS:** Relational database service for storing app data.
- **Selenium:** Testing framework for automated browser testing.

## Contributing

Contributions to the Pokemon Team Builder App are welcome! Please feel free to fork this repository, make changes, and submit a pull request. For major changes, please open an issue first to discuss the proposed changes.
