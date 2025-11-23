import json

def load_data():
    try:
        with open('youtube.txt','r') as f:
            videos=json.load(f)
            return videos
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_data_helper(videos):
    with open('youtube.txt','w') as f:
        json.dump(videos,f)

def list_all_videos(videos):
   print("\n")
   print("*"*20)
   for index,video in enumerate(videos,start=1):
         print("\n")
         print(f"{index}. Title: {video['title']}, Time: {video['time']}")


def add_video(videos):
    title = input("Enter video title: ")
    time = input("Enter video time: ")

    video = {
        "title": title,
        "time": time
    }

    videos.append(video)
    save_data_helper(videos)
    print("Video added successfully!")


def update_video(videos):
   list_all_videos(videos)
   index = int(input("Enter the index of the video to update: ")) 
   if 1<= index < len(videos):
       title = input("Enter new video title: ")
       time = input("Enter new video time: ")
       videos[index-1] = {"title": title, "time": time}

       save_data_helper(videos)
       print("Video updated successfully!")
   else:
         print("Invalid index. Please try again.")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Enter the index of the video to delete: "))
    if 1 <= index < len(videos):
        # videos.pop(index-1)
        del videos[index-1]
        save_data_helper(videos)
        print("Video deleted successfully!")
    else:
        print("Invalid index. Please try again.")

def main():

    videos=load_data()

    while True:
        print("\n youtube manager\n")
        print("1.list all youtube vidioes\n")
        print("2.add a youtube vidioes\n")    
        print("3.update a youtube vidioes\n")
        print("4.DELETE a youtube vidioes\n")
        print("5.exit the app\n")
        choice=input("enter your choice(1-5): ")
        match choice:
            case '1':
                list_all_videos(videos)
            case '2':            
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("invalid choice, please try again")
if __name__ == "__main__":
    main()



