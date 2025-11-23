import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')

def all_videos():
    cursor.execute("SELECT * FROM videos")
    rows = cursor.fetchall()
    if not rows:
        print("\nNo videos found")
    else:
        print("\nAll videos:")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Time: {row[2]}")


def add_video(name, time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()
    print("✅ Video added successfully")


def update_video(new_name, new_time, video_id):
    cursor.execute(
        "UPDATE videos SET name = ?, time = ? WHERE id = ?",
        (new_name, new_time, video_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        print("❌ No video found with that ID.")
    else:
        print("✅ Video updated successfully.")


def delete_video(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id,))
    conn.commit()
    if cursor.rowcount == 0:
        print("❌ No video found with that ID.")
    else:
        print("✅ Video deleted successfully.")


def main():
    while True:
        print("\nYouTube manager app with DB\n")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app\n")
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            all_videos()
        elif choice == 2:
            name = input("Enter video name: ")
            time = input("Enter video time: ")
            add_video(name, time)
        elif choice == 3:
            all_videos()  # 👈 pehle list dikha do taaki ID sahi do
            video_id = int(input("Enter video id to update: "))
            new_name = input("Enter new video name: ")
            new_time = input("Enter new video time: ")
            update_video(new_name, new_time, video_id)
        elif choice == 4:
            all_videos()
            video_id = int(input("Enter video id to delete: "))
            delete_video(video_id)
        elif choice == 5:
            break

    conn.close()


if __name__ == "__main__":
    main()
