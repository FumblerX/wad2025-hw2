<h2>📜Profile Redirect Web Application</h2>

This is a simple Flask-based web application that implements user authentication. After a successful login, the user is redirected to an intermediate page for 5 seconds before being taken to their profile.

<h2>🚀Features</h2>

<ol>✅ User authentication using MongoDB</ol>
<ol>✅ Session management with Flask</ol>
<ol>✅ Temporary redirect page with a countdown before loading the profile</ol>

<h2>📂Project Structure</h2>
<ul>
        <li><strong>Leyman-HW2/</strong></li>
        <ul>
            <li><strong>static/</strong>
                <ul>
                    <li>dooropen.jpg - Example image used in profile page</li>
                    <li>doorclosed.jpg - Example image used in profile page</li>
                </ul>
            </li>
            <li><strong>templates/</strong>
                <ul>
                    <li>login.html - User login page</li>
                    <li>redirect.html - Intermediate page with a countdown</li>
                    <li>profile.html - User profile page</li>
                </ul>
            </li>
            <li>app.py - Main Flask application</li>
            <li>README.md - Project documentation</li>
        </ul>
    </ul>

<h2>🛠How It Works</h2>

1. User logs in on localhost:5000/ through login.html.
2. If credentials are correct, the session is created.
3. The user is redirected to localhost:5000/redirect, where they see a countdown for 5 seconds before being taken to localhost:5000/profile.
4. The profile page welcomes the user and provides a logout option.

<h2>📷Images showing the website's work</h2>
![image](https://github.com/user-attachments/assets/6815facb-f542-48ca-9fe6-cf087e1f6513)

MongoDBCompass showing data in it.
![image](https://github.com/user-attachments/assets/52739537-7bd8-43d0-b910-eeb422dcd3fb)
Same info, but using mingosh.
![image](https://github.com/user-attachments/assets/ed44e740-7b95-4c91-b175-d2e50c7dce45)
Main page with authentication.
![image](https://github.com/user-attachments/assets/2171c7d0-06e3-47dd-af10-cd22f49c6613)
Entering correct credentials.
![image](https://github.com/user-attachments/assets/6cafb6a9-1002-4e28-b9e5-48214e681902)
The forwarding page that the user is sent to when entering correct data.
![image](https://github.com/user-attachments/assets/637d4fca-94a7-4a11-84f8-2b4bdcbfbda1)
Profile page ater redirecting a user.
![image](https://github.com/user-attachments/assets/9f5d3694-0637-4bdf-a46d-a8b209e4ad45)
Entering correct credentials of the second user.
![image](https://github.com/user-attachments/assets/2b20260a-9f08-4b52-9f6d-b8e86400254c)
The page showing the incorrect data entered





