import os


def display(directory, indent='', output_file=None, ignore_folders=None):
    folder_name = os.path.basename(directory)
    if folder_name not in ignore_folders:
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(indent + "----" + folder_name + "/\n")

    indent += "    |"

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            if os.path.basename(item_path) not in ignore_folders:
                display(item_path, indent, output_file, ignore_folders)
        else:
            if folder_name not in ignore_folders:
                with open(output_file, "a", encoding="utf-8") as file:
                    file.write(indent + "----" + item + "\n")


#! INPUT
folder_path = r"C:\Users\VuVanNghia20206205\Desktop\flask-hello-world"
folder_path = r"input"
folder_path = r"/home/vvn20206205/Desktop/Git/company20206205"
folder_path = r"C:\Users\vvn20206205\Downloads\Nghia\Git\whynotnghiavu"
# folder_path = r"C:\Users\vvn20206205\Downloads\video\Fast Typing Mastery From Beginner to Expert in 45 Minutes"
# folder_path = r"C:\Users\vvn20206205\Downloads\video\Fast_Typing_Mastery_From_Beginner_to_Expert_in_45_Minutes_2\Fast Typing Mastery From Beginner to Expert in 45 Minutes"

folder_path = r"C:\Users\vvn20206205\Downloads\video\TouchTyping\test\Udemy - Touch Typing Mastery - Learn to type correctly 2020-5"
# folder_path = r"C:\Users\vvn20206205\Downloads\video\TouchTyping\test\UdemyTouchTypingMasteryLearntotypecorrectly20205_Save"


output_file = "output.txt"
ignore_folders = [".git", "node_modules", "__pycache__"]
#! INPUT
with open(output_file, 'w', encoding="utf-8") as file:
    file.write(f"PATH: {folder_path}\n\n\n")

display(folder_path, output_file=output_file, ignore_folders=ignore_folders)
print(f"Kết quả đã được ghi vào tập tin {output_file}")
