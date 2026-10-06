import json

def load_data(filename):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(filename, "w") as f:
            json.dump([], f)
        return []

def save_data(filename, data):
        with open(filename, "w") as f:  
            json.dump(data, f, indent=4)
    
readings = load_data("data/readings.json")
notes = load_data("data/notes.json")

def log_reading(book, chapter, verse):
    reading = {
        "book": book,
        "chapter": chapter,
        "verse": verse
    }

    readings.append(reading)
    save_data("data/readings.json", readings)

def add_study_note(book, chapter, verse, note):
    study_notes = {
        "book": book,
        "chapter": chapter,
        "verse": verse,
        "note": note
    }
    
    notes.append(study_notes)
    
    save_data("data/notes.json", notes)
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
        
        log_reading(book, chapter, verse)
        
        print(f"Logged reading: {book} Chapter {chapter} Verse {verse}")
    elif choice == "2":
        print("Viewing reading history...")
        if not readings:
            print("No readings logged yet.")
        else:
            for reading in readings:
                if isinstance(reading, dict):
                    print(f"{reading['book']} Chapter {reading['chapter']} Verse {reading['verse']}")
                else:
                    print(reading)
    elif choice == "3":
        print("Adding a study note...")
        book = input("Enter the book name: ")
        chapter = input("Enter the chapter number: ")
        verse = input("Enter the verse: ")
        note = input("Enter your study note: ")
        
        add_study_note(book, chapter, verse, note)
        
        print("Study note added.")
    elif choice == "4":
        print("Viewing study notes...")
        if not notes:
            print("No study notes added yet.")
        else:
            for note in notes:
                if isinstance(note, dict):
                    print(f"{note['book']} Chapter {note['chapter']} Verse {note['verse']}: {note['note']}")
                else:
                    print(note)
    elif choice == "5":
        print("Exiting the application. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
