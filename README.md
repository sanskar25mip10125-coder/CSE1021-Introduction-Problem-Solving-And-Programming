# CSE1021-Introduction-Problem-Solving-And-Programming

-->TITLE: THE PODCAST MANEGER

--> Overview of the Project:

This project is what I built for the Intro to Problem Solving and Programming course. It's a simple, command-line tool that lets you manually track the status of       episodes across different podcasts you follow. The main focus was really getting comfortable with nested data structures—specifically, a dictionary holding lists of    episode dictionaries—and making sure all the progress saves correctly to a file. It’s written entirely in standard Python 3.

-->Features I Included:

●	Add Channels & Episodes: Basic data entry for your podcasts and their episodes.

●	Mark Progress: Easily mark an episode as completed (it's case-insensitive, which was a good little quality-of-life feature to add).

●	Global Progress Report: Get a summary of how many episodes you've finished versus how many are pending.

●	Automatic Saving: All your progress is saved automatically when you select 'Save & Exit' and reloaded when you start the app.

--> Technologies/Tools Used:

●	Language: Python 3.x

●	Libraries: Just the standard built-in json and os modules.

●	Environment: Command-Line Interface (CLI).

●	Data Storage: Local JSON file (podcast_data.json).

--> Steps to Install & Run the Project:

1.	Get the Code: Download the main.py file to your computer.
2.	Open Terminal: Navigate to the folder where you saved the file.
3.	Run: Execute the script using your Python 3 interpreter:
python3 main.py

--> Instructions for Testing:

Please try these steps to verify all the features are working:
1.	Add Data (Options 1 & 2): Add a channel (e.g., "History 101") and then add two episodes under it (e.g., "WWI Basics" and "WWII Summary").
2.	Check Status (Option 4): Use "View Episodes" to make sure both episodes show as 'Pending'.
3.	Complete One (Option 3): Mark "WWI basics" as completed. Try entering the title in lowercase to test the case-insensitivity feature!
4.	Check Report (Option 5): Verify the Global Progress Report now shows 1 Completed and 1 Pending episode (50% rate).
5.	Persistence Test (Option 6): Select "Save & Exit." Run the script again (python3 main.py). If the data loads correctly, Option 5 should still show the 50% completion rate




