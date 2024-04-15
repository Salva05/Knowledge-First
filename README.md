# Knowledge First

## Introduction
Welcome to the **Knowledge First** application. It aims to provide a platform for users to engage in discussions, share ideas, and seek assistance on various topics.

## Table of Contents
- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Yet to come](#yet-to-come)

## Getting Started

### Prerequisites
Before you begin, ensure you have met the following requirements:
- **Python 3.x:** The application is built using Python, so make sure you have Python 3.x installed on your local machine.
- **pip Package Manager:** Ensure that you have the pip package manager installed to easily install Python dependencies.
- **Django:** Django is the web framework used for building this application. You can install it globally or within a virtual environment (recommended to avoid unnecessary dependancies).

### Installation
## Step 1: Clone the Repository

1. Open your terminal or command prompt.
2. Clone this repository to your local machine using the following command:
   
   ```bash
   git clone https://github.com/Salva05/Knowledge-First.git
   ```

## Step 2: Navigate to the Project Directory

1. Change into the project directory:
    
   > **Side Note:** Be sure to run this command from the folder where the repo has been cloned

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

1. Open your web browser and navigate to `http://127.0.0.1:8000/` to access the Application.

## Issues

If you encounter any issues with the application, please feel free to open an issue on the GitHub repository.


## Usage and Features
- **Dynamic-content Home Page:** The homepage dynamically updates with fresh content triggered by significant events like new member registrations or post likes. 

![Home page](http://salvoits.altervista.org/imagesKF/HomePage.png)

- **User Registration and Authentication:** Users can register for an account and log in securely to access the forum features. Necessary fields as email, username and password will be required, so make sure to fill these fields (username and email must be unique)

![Signin-Singup](https://salvoits.altervista.org/imagesKF/singInUp.png)

- **Create and Manage Posts:** Users can create new posts, edit their own posts, and delete them if necessary. Furthermore, each post has all the side infos, included the likes; an openable window containing all the users who left a like to the post. Each of them will represent a link to their profile.

![Post's creation and edit](http://salvoits.altervista.org/imagesKF/post.png)

- **Solution Marking Mechanism:** Users can mark a reply as the solution to a post, signaling the end of discussion on that topic and providing clarity to others seeking answers. This action will automatically highlight that reply and set it as the first reply of the discussion.
> **_NOTE:_** It will set the state of the post, originary on 'Open', to 'Solved'.


![Reply marked as solution](http://salvoits.altervista.org/imagesKF/solution.png)

- **Post State:**  Posts can be in one of two states: "Open" for ongoing discussions and "Solved" once a solution has been identified and marked by the user, preventing the post from receiving further replies.

![State of the posts: Open-Solved](http://salvoits.altervista.org/imagesKF/postState.png)

- **Comments and Discussions:** Users can engage in discussions by leaving comments on posts and replying to other users' comments. It's also given the possibility to delete an answer from the post. All the replies that were replying to it will instead display a *deleted message* preventing anyone to read it anymore.

![Reply-to-reply system](http://salvoits.altervista.org/imagesKF/reply2.png)

- **Quoting System:** Users can select (drag-select) subportions of text within a reply and click "Quote" to respond directly to that portion.

![Quotuing system](http://salvoits.altervista.org/imagesKF/quote.png)

- **Categories:** Posts are categorized for easy navigation of relevant topics.

![Content page along with Categories mechanism](https://salvoits.altervista.org/imagesKF/categories.png)

- **Search Functionality:** Users can search for specific posts or topics using the search feature.

![Search functionality](http://salvoits.altervista.org/imagesKF/search.png)

- **User Profiles:** Each user has a profile page where they can view their activity and stats.

![User porfile page](http://salvoits.altervista.org/imagesKF/profile.png)

- **Members:** Every user registered in the platform will be a member, giving to anyone else the possibility to interact with him/her and to see related contents and replies.

![Member's page](http://salvoits.altervista.org/imagesKF/member.png)

- **Follow-Unfollow System:** Users can choose to follow or unfollow profiles.

- **Discussions:** A section *Discussions* will allow the user to visualize their recent activity and their topics, along with the chance to modify/delete each of them 

![Discussion's page](http://salvoits.altervista.org/imagesKF/Discussions.png)

- **Responsive Design:** The application is accessible and usable across different devices and screen sizes.

![Responsiveness demonstration, Post detail page in column layout](https://salvoits.altervista.org/imagesKF/Responsive.png)


## Technologies Used
### Backend
- **Python 3.10:** The primary programming language used for backend development.
- **Django 5.0.3:** The web framework used to build the backend of the application.
- **Pillow 10.2:** Python Imaging Library used for image processing.
- **SQLite3:** Lightweight relational database management system used as default by Django.

### Frontend
- **HTML, CSS, JavaScript:** The core technologies for building the frontend interface and interactivity.
- **jQuery 3.2.1:** JavaScript library used for simplifying DOM manipulation and event handling.
- **Bootstrap 4.0.0:** Frontend framework for building responsive and mobile-first websites.
- **Popper.js:** Dependency used in combination with Bootstrap for creating tooltips, popovers, and dropdowns.
- **Ajax 3.5:** JavaScript technique used for making asynchronous HTTP requests to the server.

## Yet to come
Below some of the future implementations that are listed to be done.

### - Improved Follow/Unfollow system:
The idea behind the improved Follow/Unfollow system is to implement a section where poeple can stay up to date with the contents published by the followers.

### - Know Who's Online:
Adding a little green circle next to member's profile pics so to know when they are connected and logged in the platform. It aims to enhance the interactions with other members.

### - Chat System:
A chat system, where the community can privately and comfortably talk with the one they follows, is behind the corner. It will be possible to start a chat only if there is a respective 'follow'.
