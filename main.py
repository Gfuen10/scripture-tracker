readings = []
with open("data/readings.txt", "r") as f:
    for line in f:
        readings.append(line.strip())
notes = []
with open("data/notes.txt", "r") as f:
    for line in f:
        notes.append(line.strip())

while True:
    print("==========================")
    print("      Scripture Tracker")
    print("==========================")
    print()
    print("1. Log today's reading")
    print("2. View reading history")
    print("3. Add a study note")
    print("4. View study notes")
    print("5. Exit")
    print()
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        print("Logging today's reading...")
        book = input("Enter the book name: ")
        chapter = input("Enter the chapter number: ")
        verse = input("Enter the verse: ")
        readings.append(f"{book} Chapter {chapter} Verse {verse}")
        with open("readings.txt", "a") as f:
            f.write(f"{book} Chapter {chapter} Verse {verse}\n")
        print(f"Logged reading: {book} Chapter {chapter} Verse {verse}")
    elif choice == "2":
        print("Viewing reading history...")
        if not readings:
            print("No readings logged yet.")
        else:
            for reading in readings:
                print(reading)
    elif choice == "3":
        print("Adding a study note...")
        book = input("Enter the book name: ")
        chapter = input("Enter the chapter number: ")
        verse = input("Enter the verse: ")
        note = input("Enter your study note: ")
        notes.append(f"{book} Chapter {chapter} Verse {verse}: {note}")
        with open("data/notes.txt", "a") as f:
            f.write(f"{book} Chapter {chapter} Verse {verse}: {note}\n")
        print("Study note added.")
    elif choice == "4":
        print("Viewing study notes...")
        if not notes:
            print("No study notes added yet.")
        else:
            for note in notes:
                print(note)
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
       

