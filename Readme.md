# Projects name 
"College Noticeboard and Results Platform" (The Scoreboard)

# Content table

1. [Description](#description)  
2. [Installation Instructions](#installation-instructions)  
3. [How to use](#how-to-use)  
4. [Technologies used](#technologies-used)  
5. [Intersting features](#intersting-features)
6. [Future features](#future-features)

# Description
This project is designed for students to view their results online. They can also access important college notices in one place.  
The website has two main sections:
### 1. Students Section  
* Students can view their results, along with PDFs of their exam papers (if provided by the college).

* They can raise questions about their results or any college-related issues.

### 2. Teachers Section  
* Teachers can upload student results.
* They can update notices on the notice board.
* Only registered teachers can sign up other teachers.
* Teachers can answer questions raised by students.

Currently, the project includes essential authentication features like login, logout, signup, and forgot password. You can use the forgot password functionality for a smoother experience.

For easy navigation, a navigation bar appears after you log in.

When you launch the website on your local machine, you'll see the notice board, student signup, and student signin options. However, the teacher signup option is hidden because anyone could potentially misuse it. To prevent unauthorized changes, teacher signup is only accessible to already registered teachers.

### Note: To experience all features, install the project on your machine.

# Installation Instructions
1. Clone the GitHub repository using the following command:  
`git clone`

2. Install the project dependencies using this command:  
```pip install -r requirements.txt```  

3. To use the forgot password functionality, update the email credentials in the `system.py` file  

4. Once you've completed the above steps, run the project with this command:  
```python manage.py runserver```

5. After running the command, open this URL in your browser:  
```http://127.0.0.1:8000/```

6. Now you can create an account by signing up and explore the website's features.

7. While teacher signup is generally restricted, you can access it by visiting this URL:  
```http://127.0.0.1:8000/signupteachers```

8. Create a teacher account and explore the teacher features.

# How to Use
###  Create Students account
1. Signup for a new student account

2. After creating your account, enter your credentials in the student login section.
3. Enter your details and submit to view your results.

4. if your details match the database information, your results will appear on the screen.

### Create teachers account
1. Visite the URL```http://127.0.0.1:8000/signupteachers``` to sign up as a teacher 

2. After successfully creating a teacher account, enter your credentials in the teacher login section.

3. Once logged in, you'll see three options: sign up a new teacher, upload student results, and update the notice board.

4. SIf you select "upload student result," a new form will appear where you can upload the results.

5. If you choose to "update the notice board," a new page will display the current notice. You can edit the notice and click submit to reflect the changes on the board.

### Add your email id and password
Please ensure to include your email ID and password in the `settings.py` file to receive the reset password link from the 'forgot password' functionality.

# Technologies used
### Backend
* Django (a python framework)

### Database
* SQLite (Django's built-in database)
### Frontend
 * HTML
 * CSS

# Intersting features
* **Separate Logins:** Students can only log in to the student section using their credentials, and teachers can only log in to the teacher section using theirs. This keeps student and teacher areas separate.

* **Student Access:** Students can view their results and submit queries, but they cannot change any data in the database.


* **Teacher Access:** Teachers can update the notice board, upload student results, and answer student queries.

* **Optional Exam PDFs:** Teachers can upload PDFs of exam papers for students to view.

* **Forgot Password:** Users can reset their forgotten passwords by entering a valid email address to receive a password reset link.


# Future Features

1. User dashboard
2. Improved user-friendliness etc. 
