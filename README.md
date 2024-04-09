# Django Forum Application

## Introduction
Welcome to the Django Forum Application! This project serves as a school project for [Your School/Class] to demonstrate proficiency in Django web development. The application provides a platform for users to engage in discussions, share ideas, and seek assistance on various topics.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites
Before you begin, ensure you have met the following requirements:
- **Python 3.x:** The application is built using Python, so make sure you have Python 3.x installed on your local machine.
- **pip Package Manager:** Ensure that you have the pip package manager installed to easily install Python dependencies.
- **Django:** Django is the web framework used for building this application. You can install it globally or within a virtual environment.

### Installation
## Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Clone this repository to your local machine using the following command:
   
   ```bash
   git clone https://github.com/Salva05/Knowledge-First.git
   ```

## Step 2: Navigate to the Project Directory

1. Change into the project directory:
    
   > **Side Note:** From the folder where the git repo has been cloned

   ```bash
   cd Knowledge-First
   ```

## Step 3: Create a Virtual Environment (Optional but Recommended)

1. It's recommended to use a virtual environment to isolate project dependencies. Create one using the following command:

   ```bash
   python3 -m venv .venv
   ```

## Step 4: Activate the Virtual Environment

1. Activate the virtual environment. Commands vary based on your operating system:

   - **On Windows:**

     ```bash
     .venv\Scripts\activate
     ```

   - **On macOS and Linux:**

     ```bash
     source .venv/bin/activate
     ```

## Step 5: Install Dependencies

1. Use pip to install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

## Step 6: Database Setup

1. Initialize the database and it's necessary elements:
   
   > **Side Note:** Be sure to run this command from the directory where the 'manage.py' file is located

   ```bash
   python manage.py migrate
   ```

## Step 7: Create Superuser (Optional)

1. If you want to access the Django admin interface, create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

## Step 8: Run the Application

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The development server will be running at `http://127.0.0.1:8000/` by default.

## Step 9: Explore the Application

1. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the Awesome Django Web Application.

## Issues

If you encounter any issues with the application, please feel free to open an issue on the GitHub repository.


## Usage
- **User Registration and Authentication:** Users can register for an account and log in securely to access the forum features.
- **Create and Manage Posts:** Users can create new posts, edit their own posts, and delete them if necessary.
- **Comments and Discussions:** Users can engage in discussions by leaving comments on posts and replying to other users' comments.
- **Categories and Tagging:** Posts are categorized and tagged for easy navigation and discovery of relevant topics.
- **Search Functionality:** Users can search for specific posts or topics using the search feature.
- **User Profiles:** Each user has a profile page where they can view their activity, edit their profile details, and manage their posts.
- **Moderation Tools:** Administrators and moderators have access to moderation tools to manage user content, including editing and deleting posts and comments.

## Features
- **User Authentication:** Allow users to register, log in, and manage their accounts.
- **Create Posts:** Users can create new posts to share their thoughts and questions.
- **Comments:** Enable users to comment on posts for discussions.
- **Categories:** Categorize posts for easier navigation and organization.
- **Tags:** Tag posts with keywords for better categorization and searchability.
- **Search:** Provide a search feature to find posts based on keywords.
- **Moderation:** Allow moderators to manage posts and comments, including editing and deleting.
- **User Profiles:** Users can view and edit their profiles, including profile pictures and bio.
- **Notifications:** Notify users about new comments, replies, or other relevant activities.
- **Responsive Design:** Ensure the application is accessible and usable across different devices and screen sizes.

## Technologies Used
### Backend
- **Python 3.10:** The primary programming language used for backend development.
- **Django 5.0.3:** The web framework used to build the backend of the application.
- **Pillow 10.2:** Python Imaging Library used for image processing.
- **SQLite3:** Lightweight relational database management system used for local development.

### Frontend
- **HTML, CSS, JavaScript:** The core technologies for building the frontend interface and interactivity.
- **jQuery 3.2.1:** JavaScript library used for simplifying DOM manipulation and event handling.
- **Bootstrap 4.0.0:** Frontend framework for building responsive and mobile-first websites.
- **Popper.js:** Dependency used in combination with Bootstrap for creating tooltips, popovers, and dropdowns.
- **Ajax 3.5:** JavaScript technique used for making asynchronous HTTP requests to the server.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. **Fork the repository.**
2. **Create a new branch for your feature (`git checkout -b feature/AmazingFeature`).**
3. **Commit your changes (`git commit -m 'Add some AmazingFeature'`).**
4. **Push to the branch (`git push origin feature/AmazingFeature`).**
5. **Open a pull request.**

## License
This project is licensed under the [Your License Name] License - see the `LICENSE` file for details.
