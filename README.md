# Automatically Sending Message app on Whatsapp
Assalam-U-Alaikum</br>
I have created an app in which we can send a message on bulk automatically. This app will send message to each user after 15 seconds and we can extend the time of sending the message to each user. The Streamlit UI is used in the project which is a web based module in Python. This program can also send Images with the Captions. I have separated it in two pages which is:</br>
1. Only Text
2. Text and Images

List of Libraries which used in the implementation of this app:</br>
1️⃣ Pywhatkit: This library is used to send messages automatically. It takes messages as an input and the phone numbers of users in whatsapp to whom we want to send the message. The function of this library is to open browser automatically and send the message to the given number. This library can close Whatsapp tab if we give him the closetab time.</br>
2️⃣ Streamlit: This library is used to make web based applications and make an interactive UI for developers and users to interact with. This library is mostly used for Data Analysis and this types of working.</br>
3️⃣ Time: This library is used in this project to maintain working of some step during sending the message.</br>
4️⃣ Keyboard: This is used to check whether the specific button is pressed or not to continue the process of sending the message.</br>
5️⃣ Pyautogui: This is used to automatically press some buttons of keyboard when some process is done.</br>
6️⃣ Tempfile: This is used to remove the previous file which is send previously to the previous users.</br>
7️⃣ os: This module is used to start the app when double click on the icon of this app.
