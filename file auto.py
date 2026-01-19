import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import logging

# Set up logging
logging.basicConfig(filename='file_organizer.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Dictionary to map file extensions to their respective folders
extension_folders = {
    # Images
    '.jpeg': 'images',
    '.jpg': 'images',
    '.png': 'images',
    '.gif': 'images',
    '.bmp': 'images',
    '.tiff': 'images',

    # Documents
    '.doc': 'documents',
    '.docx': 'documents',
    '.pdf': 'documents',
    '.txt': 'documents',
    '.rtf': 'documents',
    '.xlsx': 'documents',
    '.ppt': 'documents',
    '.pptx': 'documents',

    # Archives
    '.zip': 'archives',
    '.rar': 'archives',
    '.7z': 'archives',
    '.tar': 'archives',
    '.gz': 'archives',

    # Code
    '.c': 'code',
    '.cpp': 'code',
    '.py': 'code',
    '.java': 'code',
    '.js': 'code',
    '.html': 'code',
    '.css': 'code',
    '.php': 'code',

    # Executables
    '.exe': 'executables',
    '.dll': 'executables',

    # Audio
    '.mp3': 'audio',
    '.wav': 'audio',
    '.flac': 'audio',

    # Video
    '.mp4': 'video',
    '.avi': 'video',
    '.mkv': 'video',

    # Databases
    '.sql': 'databases',

    # Applications
    '.app': 'applications',

    # Data
    '.json': 'data',

    # Virtual Disk Images
    '.iso': 'disk_images',

    # Other
    '.csv': 'data',
    '.log': 'logs',
    '.xml': 'xml',
    '.svg': 'images',

    # Add more extensions and corresponding folders as needed
}

# Define the function to organize files
def organize_files():
    selected_directory = filedialog.askdirectory()

    if selected_directory:
        destination_folder = os.path.join(selected_directory, "organized_files")
        if not os.path.exists(destination_folder):
            os.mkdir(destination_folder)
            logging.info(f"Created directory: {destination_folder}")

        # Function to move a file to the appropriate folder
        def move_file(file_path, destination_folder):
            if not os.path.exists(destination_folder):
                os.mkdir(destination_folder)
                logging.info(f"Created directory: {destination_folder}")
            base_name = os.path.basename(file_path)
            destination_path = os.path.join(destination_folder, base_name)
            if os.path.exists(destination_path):
                name, ext = os.path.splitext(base_name)
                counter = 1
                new_name = f"{name}_{counter}{ext}"
                new_destination_path = os.path.join(destination_folder, new_name)
                while os.path.exists(new_destination_path):
                    counter += 1
                    new_name = f"{name}_{counter}{ext}"
                    new_destination_path = os.path.join(destination_folder, new_name)
                destination_path = new_destination_path
            shutil.move(file_path, destination_path)
            logging.info(f"Moved {file_path} to {destination_path}")

        total_files = len([name for name in os.listdir(selected_directory) if os.path.isfile(os.path.join(selected_directory, name))])
        progress['maximum'] = total_files

        for count, filename in enumerate(os.listdir(selected_directory)):
            file_path = os.path.join(selected_directory, filename)
            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(filename)
                if file_extension.lower() in extension_folders:
                    destination = os.path.join(destination_folder, extension_folders[file_extension.lower()])
                    move_file(file_path, destination)
                else:
                    move_file(file_path, os.path.join(destination_folder, 'other'))
            progress['value'] = count + 1
            root.update_idletasks()

        messagebox.showinfo("Information", f"Files have been organized in {destination_folder}")
        logging.info("File organization complete")

# Define the function to configure extension mappings
def configure_extensions():
    config_window = tk.Toplevel(root)
    config_window.title("Configure Extensions")

    def save_config():
        for ext, folder_var in extension_entries.items():
            extension_folders[ext] = folder_var.get()
        config_window.destroy()

    extension_entries = {}
    for ext, folder in extension_folders.items():
        frame = ttk.Frame(config_window)
        frame.pack(pady=5)
        ext_label = ttk.Label(frame, text=ext)
        ext_label.pack(side='left', padx=5)
        folder_var = tk.StringVar(value=folder)
        folder_entry = ttk.Entry(frame, textvariable=folder_var)
        folder_entry.pack(side='left', padx=5)
        extension_entries[ext] = folder_var

    save_button = ttk.Button(config_window, text="Save", command=save_config)
    save_button.pack(pady=10)

# Define the function to preview changes
def preview_changes():
    selected_directory = filedialog.askdirectory()
    if selected_directory:
        preview_window = tk.Toplevel(root)
        preview_window.title("Preview Changes")
        preview_text = tk.Text(preview_window, wrap='word', height=20, width=80)
        preview_text.pack(padx=10, pady=10)
        
        for filename in os.listdir(selected_directory):
            file_path = os.path.join(selected_directory, filename)
            if os.path.isfile(file_path):
                _, file_extension = os.path.splitext(filename)
                if file_extension.lower() in extension_folders:
                    destination = os.path.join("organized_files", extension_folders[file_extension.lower()], filename)
                else:
                    destination = os.path.join("organized_files", 'other', filename)
                preview_text.insert(tk.END, f"{file_path} -> {destination}\n")

# Create a Tkinter root window
root = tk.Tk()
root.title("File Organizer")
root.geometry("600x400")

# Create a frame for better organization of widgets
frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(expand=True, fill='both')

# Create a title label
title_label = ttk.Label(frame, text="File Organizer", font=("Helvetica", 32))
title_label.pack(pady=10)

# Create a description label
description_label = ttk.Label(frame, text="Select a directory to organize files into respective folders based on their extensions.")
description_label.pack(pady=10)

# Create a progress bar
progress = ttk.Progressbar(frame, orient='horizontal', length=400, mode='determinate')
progress.pack(pady=20)

# Create a button to start the file organization process
organize_button = ttk.Button(frame, text="Select Directory and Organize Files", command=organize_files)
organize_button.pack(pady=5)

# Create a button to configure extension mappings
configure_button = ttk.Button(frame, text="Configure Extensions", command=configure_extensions)
configure_button.pack(pady=5)

# Create a button to preview changes
preview_button = ttk.Button(frame, text="Preview Changes", command=preview_changes)
preview_button.pack(pady=5)

# Run the Tkinter main loop
root.mainloop()
