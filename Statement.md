Project Statement: Podcast Episode Manager

--> Problem Statement: 

As a user tracking multiple podcasts, it quickly gets confusing to remember which episodes have been listened to across different shows. The core problem this project addresses is the lack of a simple, central utility to log podcast channels and manage the completion status of their episodes. My solution aims to be a foundational programming exercise that tackles this organization issue using nested data structures (dictionaries and lists) and reliable file handling in Python.

--> Scope of the Project:

The Podcast Episode Manager is scoped as a Command-Line Interface (CLI) application. It focuses entirely on data management and reporting. All data is stored in a local JSON file (podcast_data.json).
In Scope:
●	Adding/removing (conceptually, by tracking status) channel and episode records.
●	Updating episode status (Pending \to Completed).
●	Calculating and displaying basic global progress metrics (totals and completion rate).
Out of Scope:
●	Any form of internet connectivity (e.g., RSS feed reading).
●	Graphical User Interface (GUI).
●	Advanced features like deleting records, sorting, or date-based filtering.

--> Target Users:

The primary users are anyone who wants a straightforward, non-automated system to track their media consumption progress, particularly students who need a minimal, functional tool for organization.

--> High-Level Features:

1.	Channel Registration: Ability to add new podcast feeds.
2.	Episode Logging: Manually add episode titles and release dates to a channel.
3.	Completion Status: Mark episodes as finished, using a simple title match.
4.	Progress Reporting: Generate an overall completion percentage report.
5.	Data Persistence: Automatic saving and loading of all data using JSON.

