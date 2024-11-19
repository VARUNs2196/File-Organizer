import os
import tkinter as tk
from tkinter import messagebox, PhotoImage

# Function to organize files in the specified directory based on selected types
def organize_files(directory, selected_types):
    # Detect the operating system using os.name
    is_windows = os.name == 'nt'
    
    # Define file categories and corresponding file extensions
    file_types = {
        'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
        'Audios': ['.mp3', '.wav', '.aac', '.flac'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
    }

    # Create folders for each selected file category if they don't already exist
    for folder in selected_types:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    # Iterate over the files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        # Skip directories
        if os.path.isdir(file_path):
            continue
        
        # Determine the file extension
        file_extension = os.path.splitext(file_name)[1].lower()
        
        # Initialize moved flag to False for each file
        moved = False
        
        # Check for Videos category
        if 'Videos' in selected_types:
            if file_extension in file_types['Videos']:
                destination = os.path.join(directory, 'Videos', file_name)
                if not os.path.exists(destination):
                    if is_windows:
                        os.system(f'move "{file_path}" "{destination}"')
                    else:
                        os.system(f'mv "{file_path}" "{destination}"')
                moved = True  # Mark as moved
        
        # Check for Audios category
        if not moved and 'Audios' in selected_types:
            if file_extension in file_types['Audios']:
                destination = os.path.join(directory, 'Audios', file_name)
                if not os.path.exists(destination):
                    if is_windows:
                        os.system(f'move "{file_path}" "{destination}"')
                    else:
                        os.system(f'mv "{file_path}" "{destination}"')
                moved = True  # Mark as moved
        
        # Check for Documents category
        if not moved and 'Documents' in selected_types:
            if file_extension in file_types['Documents']:
                destination = os.path.join(directory, 'Documents', file_name)
                if not os.path.exists(destination):
                    if is_windows:
                        os.system(f'move "{file_path}" "{destination}"')
                    else:
                        os.system(f'mv "{file_path}" "{destination}"')
                moved = True  # Mark as moved

        # If no matching category was found and Miscellaneous is selected, move to Miscellaneous
        if not moved and 'Miscellaneous' in selected_types:
            misc_destination = os.path.join(directory, 'Miscellaneous', file_name)
            if not os.path.exists(misc_destination):
                if is_windows:
                    os.system(f'move "{file_path}" "{misc_destination}"')
                else:
                    os.system(f'mv "{file_path}" "{misc_destination}"')

    messagebox.showinfo("Success", "Files have been organized!")

# Function to handle button click event
def show_input():
    user_input = entry.get()  # Get text from the entry box
    selected_types = [file_type for var, file_type in zip(check_vars, list(file_types.keys()) + ['Miscellaneous']) if var.get()]
    
    if not selected_types:
        messagebox.showwarning("Warning", "Please select at least one type of file to organize.")
        return
    
    if os.path.exists(user_input):
        organize_files(user_input, selected_types)
    else:
        messagebox.showerror("Error", "Invalid directory path!")

# Create main application window
root = tk.Tk()
root.title("File Organizer")
root.geometry("500x300")  # Set the window size

# Set background image (make sure to have an image named 'background.png' in the same directory)
bg_image = PhotoImage(file=r"C:\Users\VARUN\Desktop\pooja\organizer.png")  # Replace with your image path
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

# Create label and entry for user input with Arial Bold font
label = tk.Label(root, text="Enter directory path to organize:", bg='white', font=('Arial', 12, 'bold'))
label.pack(pady=20)

entry = tk.Entry(root, width=50, font=('Arial', 12))
entry.pack(pady=10)

# Define checkboxes for each file type in a horizontal layout
file_types = {
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Audios': ['.mp3', '.wav', '.aac', '.flac'],
    'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt'],
}

check_vars = []
checkbox_frame = tk.Frame(root, bg='white')
checkbox_frame.pack(pady=20)

for file_type in list(file_types.keys()) + ['Miscellaneous']:  # Include Miscellaneous as an option.
    var = tk.BooleanVar()
    check_vars.append(var)
    cb = tk.Checkbutton(checkbox_frame, text=file_type, variable=var, bg='white',
                        font=('Arial', 10, 'bold'))
    cb.pack(side=tk.LEFT)

# Checkbox for "Select All" option placed in the same row
def select_all():
    all_selected = all(var.get() for var in check_vars)
    for var in check_vars:
        var.set(not all_selected)

all_var = tk.BooleanVar()
all_cb = tk.Checkbutton(checkbox_frame, text="Select All", variable=all_var,
                         command=select_all, bg='white',
                         font=('Arial', 10, 'bold'))
all_cb.pack(side=tk.LEFT)  # Pack it to align with other checkboxes

# Create submit button with Arial Bold font
button = tk.Button(root, text="Organize Files", command=show_input,
                   font=('Arial', 12, 'bold'))
button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
