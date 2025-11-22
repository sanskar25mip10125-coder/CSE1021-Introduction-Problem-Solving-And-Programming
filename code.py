# ----------------------------------------------------------
# PODCAST EPISODE MANAGER
# Intro to Problem Solving & Programming (Python Project)
# ----------------------------------------------------------

# Data structure:
# channels = {
#    "Channel Name": [
#        {"title": "Episode Name", "date": "dd-mm-yyyy", "status": "Pending"},
#        ...
#    ]
# }

channels = {}


# ---------------------- Add Channel -----------------------
def add_channel():
    name = input("Enter channel name: ").strip()

    if name in channels:
        print("Channel already exists!\n")
    else:
        channels[name] = []
        print("Channel added successfully!\n")


# ----------------------- Add Episode ----------------------
def add_episode():
    channel = input("Enter channel name: ").strip()

    if channel not in channels:
        print("Channel not found!\n")
        return

    title = input("Enter episode title: ").strip()
    date = input("Enter episode release date (dd-mm-yyyy): ").strip()

    episode = {
        "title": title,
        "date": date,
        "status": "Pending"
    }

    channels[channel].append(episode)
    print("Episode added successfully!\n")


# -------------------- Mark as Completed -------------------
def mark_completed():
    channel = input("Enter channel name: ").strip()

    if channel not in channels:
        print("Channel not found!\n")
        return

    title = input("Enter episode title to mark completed: ").strip()

    for ep in channels[channel]:
        if ep["title"].lower() == title.lower():
            ep["status"] = "Completed"
            print("Episode marked as completed!\n")
            return

    print("Episode not found!\n")


# ---------------------- View Episodes ---------------------
def view_episodes():
    channel = input("Enter channel name: ").strip()

    if channel not in channels:
        print("Channel not found!\n")
        return

    episodes = channels[channel]

    if not episodes:
        print("No episodes added yet.\n")
        return

    print(f"\nEpisodes in '{channel}':")
    print("-------------------------------------")
    for ep in episodes:
        print("Title :", ep["title"])
        print("Date  :", ep["date"])
        print("Status:", ep["status"])
        print("-------------------------------------")
    print()


# -------------------- Progress Report ----------------------
def show_progress():
    total = 0
    completed = 0

    for channel in channels:
        for ep in channels[channel]:
            total += 1
            if ep["status"] == "Completed":
                completed += 1

    pending = total - completed

    print("\n----- Podcast Progress Report -----")
    print("Total Episodes   :", total)
    print("Completed         :", completed)
    print("Pending           :", pending)
    print("-----------------------------------\n")


# ------------------------- Menu Loop -----------------------
def main_menu():
    while True:
        print("=== PODCAST EPISODE MANAGER ===")
        print("1. Add Podcast Channel")
        print("2. Add Episode")
        print("3. Mark Episode as Completed")
        print("4. View Episodes")
        print("5. View Progress Report")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_channel()
        elif choice == "2":
            add_episode()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            view_episodes()
        elif choice == "5":
            show_progress()
        elif choice == "6":
            print("Thank you for using the Podcast Episode Manager!")
            break
        else:
            print("Invalid option. Please try again.\n")


# ------------------------- Program Start -------------------
main_menu()
