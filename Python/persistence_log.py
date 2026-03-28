import csv

def Daily_Blocker(contend):
    try:
            # Use 'a' (append) instead of 'w' if you want to add text without overwriting the previous file.
            #Or keep 'w' if you prefer to always overwrite the file.
            with open('Data/Database.txt', 'a', newline='', encoding='utf-8') as file:
                  file.write(contend.strip() + '\n')  # Write the content followed by a newline character
                  print("Data saved correctly.")
    except Exception as e:
        print(f"Error occurred while writing: {e}")

def Fetch():
      with open('Data/Database.txt', 'r', newline='', encoding='utf-8') as file:
            file.seek(0)  # Move the cursor to the beginning of the file
            data = file.read()  # Read the entire content of the file
            print("Data fetched correctly.")
            return data

print(Fetch())


# Fetch: search database.txt for all records saved using this command and display them in the console. print(Fetch())
# Overwrite: Deletes everything in the file and writes from scratch.
# Persistence and Reach out: If an error is displayed, the error is sent to the user via the console to avoid future errors, maintaining the persistence of the stored data.