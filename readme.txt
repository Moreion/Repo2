App to create an Excel spreadsheet with your Ranked Data and other stuff

Credits to Farzain M. for the initial build and some of the readme instructions

BEFORE YOU RUN THE PROGRAM

Before doing anything, we need to install a module called "requests" and "openpyxl". Requests allows the program to grab data from Riots API and Openyxl allow us to write/read data from the spreadsheet. Without any of them, the program WILL NOT WORK.

STEP ONE
Download Python Version 2.7.10: https://www.python.org/downloads/ If its the first time you install Python I recommend to restart your computer. This helped me to solve install problems.

STEP TWO
Awesome, now you have Python! Now go to your Command Prompt or Terminal. Once your in your Terminal, simply type in "python" and press enter. 
If you get this error: 'python' is not recognized as an internal or external command, operable program or batch file.
Then you need to change your enviroment variables. There is an awesome walkthrough on how to do that here: http://pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/
After, type in "python" in command line to ensure you did this correctly. You should see stuff.  Close and reopen Command Prompt. 

STEP THREE
In your Terminal change your directory (using the "cd" command) to where my program and all its files are. For example, if the file is on your Desktop type in: cd C:\Users\(ENTER YOUR COMPUTERS NAME HERE)\Desktop\Repo2

STEP FOUR
We need to install pip. So once your in my programs directory, type in: python get-pip.py

STEP FIVE
Now go ahead in Terminal and type in: pip
If you get this error: 'pip' is not recognized as an internal or external command, operable program or batch file.
Then you need to change your enviroment variables. You can do this using the same method you used to add Python above. Except this time, once your in Enviroment Variables, click PATH, then Edit, and add your Python 
scripts path.  Mines is "C:\Python27\Scripts".  Type in "pip" in command line to ensure you did this correctly. You should see stuff. Close and reopen Command Prompt. 

STEP SIX
Install requests. Simply type in "pip install requests"

STEP SEVEN
Install openyxl. Type in "pip install openyxl"

Feel free to message me on Hangouts moreion@gmail.com